#!/usr/bin/env python3
"""Fuegt das Modern-Farbsystem (Farbthemen + 5 Einzelfarben) in den Skin ein. Idempotent."""
import re
B = '/home/claude/skins/azm/1080i/'
THEMES = [  # key, string-id, Hintergrund, Oberflaechen, Fokus, Text auf Fokus, Akzent
    ("graphit", 32161, "ff101317", "1effffff", "fff1f3f5", "ff14171b", "ff9db0cf"),
    ("mitternacht", 32162, "ff0b1220", "24a8c4ff", "ffdce8ff", "ff0b1220", "ff8fb4ff"),
    ("oled", 32163, "ff000000", "1affffff", "ffffffff", "ff000000", "ffa0a0a0"),
    ("nordlicht", 32164, "ff08171a", "2280e0c8", "ffbff0dd", "ff08201a", "ff7fd6b9"),
    ("sonnenuntergang", 32165, "ff1a1016", "24ffb4a2", "ffffc4b0", "ff2a1016", "ffffa78c"),
    ("sand", 32166, "ff17140f", "22f1e3c8", "fff1e3c8", "ff201a10", "ffd6c39c"),
    ("kodiblau", 32167, "ff0f1419", "1effffff", "ff1f8fff", "ffffffff", "ff6fb6ff"),
]
VARS = ["ModernBg", "ModernSurface", "ModernFocus", "ModernFocusText", "ModernAccent"]

def rw(f, fn):
    s = open(B + f, encoding='utf-8').read(); n = fn(s)
    if n != s: open(B + f, 'w', encoding='utf-8').write(n)

def defs(d):
    if 'name="ModernBg"' in d: return d
    v = '    <!-- Modern: Farbsystem (Skin-Einstellungen > Farben) -->\n'
    for i, name in enumerate(VARS):
        v += (f'    <variable name="{name}">\n        <value condition="!String.IsEmpty(Skin.String({name}))">$INFO[Skin.String({name})]</value>\n'
              f'        <value>{THEMES[0][2 + i]}</value>\n    </variable>\n')
    d = d.replace('    <!-- Modern: schlichter weisser Fokusrahmen', v + '\n    <!-- Modern: schlichter weisser Fokusrahmen', 1)
    return d.replace('<variable name="ColorFocusFrame">\n        <value>fff2f2f2</value>', '<variable name="ColorFocusFrame">\n        <value>$VAR[ModernFocus]</value>')
rw('Includes_Defs.xml', defs)

def items(it):
    if 'CustomSettings_Items.ModernTheme' in it: return it
    x = '    <include name="CustomSettings_Items.ModernTheme">\n'
    for key, sid, *cols in THEMES:
        x += f'        <item>\n            <label>$LOCALIZE[{sid}]</label>\n            <property name="SettingsName">$LOCALIZE[32160]</property>\n'
        x += f'            <onclick>Skin.SetString(ModernTheme,{key})</onclick>\n'
        for name, c in zip(VARS, cols):
            x += f'            <onclick>Skin.SetString({name},{c})</onclick>\n'
        x += '            <onclick>Close</onclick>\n'
        cond = (f'String.IsEqual(Skin.String(ModernTheme),{key})' if key != 'graphit'
                else '[String.IsEmpty(Skin.String(ModernTheme)) | String.IsEqual(Skin.String(ModernTheme),graphit)]')
        x += f'            <include condition="{cond}">Item_Selected</include>\n        </item>\n'
    x += '    </include>\n\n'
    return it.replace('    <include name="CustomSettings_Items.OSD_Timeout">', x + '    <include name="CustomSettings_Items.OSD_Timeout">', 1)
rw('Includes_Items.xml', items)

def dlg(c):
    if 'ModernTheme' in c: return c
    line = '<include condition="String.IsEqual(Window(Home).Property(includesetting),OSD_Timeout)">CustomSettings_Items.OSD_Timeout</include>'
    ind = re.search(r'(\s*)' + re.escape(line), c).group(1)
    return c.replace(line, line + ind + '<include condition="String.IsEqual(Window(Home).Property(includesetting),ModernTheme)">CustomSettings_Items.ModernTheme</include>', 1)
rw('Custom_1130_DialogSelect.xml', dlg)

def labels(l):
    if 'Label_ModernTheme' in l: return l
    v = '    <variable name="Label_ModernTheme">\n'
    for key, sid, *_ in THEMES[1:]:
        v += f'        <value condition="String.IsEqual(Skin.String(ModernTheme),{key})">$LOCALIZE[{sid}]</value>\n'
    v += '        <value condition="String.IsEqual(Skin.String(ModernTheme),custom)">$LOCALIZE[32168]</value>\n'
    v += f'        <value>$LOCALIZE[{THEMES[0][1]}]</value>\n    </variable>\n\n'
    return l.replace('    <variable name="Label_OSDStyle">', v + '    <variable name="Label_OSDStyle">', 1)
rw('Includes_Labels.xml', labels)

S = [(32160, "Colour theme", "Farbthema"), (32161, "Graphite (default)", "Graphit (Standard)"), (32162, "Midnight", "Mitternacht"),
     (32163, "OLED black", "OLED Schwarz"), (32164, "Northern lights", "Nordlicht"), (32165, "Sunset", "Sonnenuntergang"),
     (32166, "Sand", "Sand"), (32167, "Kodi blue", "Kodi-Blau"), (32168, "Custom", "Benutzerdefiniert"),
     (32169, "Background", "Hintergrund"), (32170, "Surfaces (tiles, panels)", "Oberflächen (Kacheln, Panels)"),
     (32171, "Focus and buttons", "Fokus und Buttons"), (32172, "Text on focus", "Text auf Fokus"),
     (32173, "Accent (headings, chapters)", "Akzent (Überschriften, Kapitel)"), (32174, "Reset colours", "Farben zurücksetzen"),
     (32175, "Modern colours", "Modern-Farben")]
for lang, de in (("en_gb", False), ("de_de", True)):
    p = f'/home/claude/skins/azm/language/resource.language.{lang}/strings.po'
    t = open(p, encoding='utf-8').read()
    if '#32160' in t: continue
    t = t.rstrip('\n') + '\n\n' + '\n'.join(f'msgctxt "#{i}"\nmsgid "{e}"\nmsgstr "{d if de else ""}"\n' for i, e, d in S)
    open(p, 'w', encoding='utf-8').write(t)
print("ok")
