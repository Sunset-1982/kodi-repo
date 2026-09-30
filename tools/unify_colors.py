#!/usr/bin/env python3
"""Verbindet die Original-Farbvariablen (ColorHighlight, ColorGradient, Selected-Text) mit dem Modern-Farbsystem.
Thema 'classic' (Skin.String(ModernTheme)=classic) stellt die Original-Farben wieder her. Idempotent."""
import re, glob
B = '/home/claude/skins/azm/1080i/'
GENERATED = {'Includes_OSDModern.xml', 'Includes_SettingsModern.xml'}
MOD = '!String.IsEqual(Skin.String(ModernTheme),classic)'

# 1) Variablen
d = open(B + 'Includes_Defs.xml', encoding='utf-8').read()
if 'name="ColorHighlightText"' not in d:
    d = d.replace('''    <variable name="ColorHighlight">
        <value condition="!String.IsEmpty(Skin.String(focuscolor.name))">$INFO[Skin.String(focuscolor.name)]</value>''',
f'''    <variable name="ColorHighlight">
        <value condition="{MOD}">$VAR[ModernFocus]</value>
        <value condition="!String.IsEmpty(Skin.String(focuscolor.name))">$INFO[Skin.String(focuscolor.name)]</value>''', 1)
    d = d.replace('''    <variable name="ColorGradient">
''', f'''    <variable name="ColorGradient">
        <value condition="{MOD}">$VAR[ModernFocus]</value>
''', 1)
    d = d.replace('    <!-- Modern: Farbsystem', f'''    <!-- Modern: Text auf Fokusflaechen und hervorgehobener Text -->
    <variable name="ColorHighlightText">
        <value condition="{MOD}">$VAR[ModernFocusText]</value>
        <value>Selected</value>
    </variable>
    <variable name="ColorAccentText">
        <value condition="{MOD}">$VAR[ModernAccent]</value>
        <value>$VAR[ColorHighlight]</value>
    </variable>

    <!-- Modern: Farbsystem''', 1)
    open(B + 'Includes_Defs.xml', 'w', encoding='utf-8').write(d)

# 2) Texte auf Fokusbalken + hervorgehobener Text
stats = {}
for f in glob.glob(B + '*.xml'):
    name = f.split('/')[-1]
    if name in GENERATED: continue
    s = open(f, encoding='utf-8').read(); o = s
    # Fokus-Layouts mit Highlight-Flaeche: helle Textfarben -> Text auf Fokus
    def fl(m):
        b = m.group(0)
        if 'ColorHighlight' not in b and 'ColorGradient' not in b: return b
        b = re.sub(r'<textcolor>(Selected|PanelWhite100|PanelWhite70|Dark1|Dark2|Light1|Light2|Black70|Black100)</textcolor>', '<textcolor>$VAR[ColorHighlightText]</textcolor>', b)
        return re.sub(r'<selectedcolor>(Selected|PanelWhite100|PanelWhite70|Dark1|Dark2|Light1|Light2|Black70|Black100)</selectedcolor>', '<selectedcolor>$VAR[ColorHighlightText]</selectedcolor>', b)
    s = re.sub(r'<focusedlayout.*?</focusedlayout>', fl, s, flags=re.S)
    s = re.sub(r'<(textureradioonfocus|textureradioofffocus|textureradiofocus)( [^>]*)?colordiffuse="(FFFFFFFF|ffffffff|Selected|PanelWhite100)"', r'<\1\2colordiffuse="$VAR[ColorHighlightText]"', s)
    s = s.replace('<focusedcolor>Selected</focusedcolor>', '<focusedcolor>$VAR[ColorHighlightText]</focusedcolor>')
    # hervorgehobener Text -> Akzent (nicht in Flaechen/Texturen)
    s = s.replace('<textcolor>$VAR[ColorHighlight]</textcolor>', '<textcolor>$VAR[ColorAccentText]</textcolor>')
    s = s.replace('[COLOR=$VAR[ColorHighlight]]', '[COLOR=$VAR[ColorAccentText]]')
    if s != o:
        open(f, 'w', encoding='utf-8').write(s); stats[name] = 1
print("geaenderte Dateien:", len(stats))

# 3) Fokusbalken der Ansichten (box.png in Dark1) -> Fokusfarbe, Text darauf -> Text auf Fokus
d = open(B + 'Includes_Defs.xml', encoding='utf-8').read()
if 'name="ColorListFocus"' not in d:
    d = d.replace('    <!-- Modern: Farbsystem', f'''    <variable name="ColorListFocus">
        <value condition="{MOD}">$VAR[ModernFocus]</value>
        <value>Dark1</value>
    </variable>
    <variable name="ColorListFocusText">
        <value condition="{MOD}">$VAR[ModernFocusText]</value>
        <value>Light1</value>
    </variable>
    <variable name="ColorListFocusText2">
        <value condition="{MOD}">$VAR[ModernFocusText]</value>
        <value>Light2</value>
    </variable>

    <!-- Modern: Farbsystem''', 1)
    open(B + 'Includes_Defs.xml', 'w', encoding='utf-8').write(d)
n3 = 0
for f in glob.glob(B + '*.xml'):
    name = f.split('/')[-1]
    if name in GENERATED: continue
    s = open(f, encoding='utf-8').read(); o = s
    def lf(m):
        b = m.group(0)
        if not re.search(r'colordiffuse="Dark1"[^>]*>common/box\.png', b): return b
        b = re.sub(r'(<texture[^>]*?)colordiffuse="Dark1"([^>]*>common/box\.png)', r'\1colordiffuse="$VAR[ColorListFocus]"\2', b)
        b = re.sub(r'<(textcolor|selectedcolor)>Light1</\1>', r'<\1>$VAR[ColorListFocusText]</\1>', b)
        b = re.sub(r'<(textcolor|selectedcolor)>Light2</\1>', r'<\1>$VAR[ColorListFocusText2]</\1>', b)
        return b
    s = re.sub(r'<focusedlayout.*?</focusedlayout>', lf, s, flags=re.S)
    s = re.sub(r'<include name="[^"]*[Ff]ocus[^"]*">.*?</include>', lf, s, flags=re.S)
    if s != o:
        open(f, 'w', encoding='utf-8').write(s); n3 += 1
print("Ansichten-Fokus angepasst in Dateien:", n3)
