#!/usr/bin/env python3
"""Erzeugt 1080i/Includes_SettingsModern.xml (Arctic Zephyr - Modern).
Einstellungs-Designs: A = Schwebend (Skin.String(SettingsStyle) leer), B = Seitenblatt, C = Karten.
Aufruf im Skin-Ordner:  python3 ../tools/gen_settings_modern.py
"""
import re, sys

SKIN = sys.argv[1] if len(sys.argv) > 1 else "."
OUT = f"{SKIN}/1080i/Includes_SettingsModern.xml"

W, DARK, TXT, MUTED, DIM, ACC = "fff1f3f5", "ff14171b", "ffececec", "ff98a0aa", "ff6c747e", "ff9db0cf"
DIS = "59ececec"

# ------------------------------------------------------------ Hub-Items umsortieren
items_xml = open(f"{SKIN}/1080i/Includes_Items.xml", encoding="utf-8").read()
blk = re.search(r'<include name="SettingsInfoItems">(.*?)</include>', items_xml, re.S).group(1)
ITEMS = {m.group(1): m.group(0) for m in re.finditer(r'<item id="(\d+)">.*?</item>', blk, re.S)}
CE = "System.HasAddon(service.coreelec.settings)"

def item(i, extra_visible=None, new_id=None):
    x = ITEMS[i]
    if new_id:
        x = x.replace(f'<item id="{i}">', f'<item id="{new_id}">', 1)
    if extra_visible:
        if "<visible>" in x:
            x = re.sub(r"<visible>(.*?)</visible>", lambda m: f"<visible>[{m.group(1)}] + {extra_visible}</visible>", x, 1)
        else:
            x = x.replace("</item>", f"    <visible>{extra_visible}</visible>\n        </item>")
    return "        " + x

ORDER_ALL = ["1", "2", "6", "12", "11", "5", "8", "13", "7", "4", "10", "9", "14", "3"]
items_modern = "\n".join(item(i) for i in ORDER_ALL)
items_top = "\n".join([item("1"), item("2"), item("6"), item("12"), item("14", f"!{CE}")])
items_rest = "\n".join([item(i) for i in ["5", "8", "13", "7", "4", "10", "11", "9", "3"]] + [item("14", CE)])

# ------------------------------------------------------------ Bausteine
def lbl(left, top, width, height, font, color, label, extra="", align="left"):
    return f"""
        <control type="label">
            <left>{left}</left><top>{top}</top><width>{width}</width><height>{height}</height>
            <font>{font}</font><textcolor>{color}</textcolor><align>{align}</align>
            <label>{label}</label>{extra}
        </control>"""

def tbox(left, top, width, height, font, color, label, cid=None, auto=True):
    idattr = f' id="{cid}"' if cid else ""
    lab = f"\n            <label>{label}</label>" if label else ""
    sc = '\n            <autoscroll delay="4000" repeat="8000" time="3000" />' if auto else ""
    return f"""
        <control type="textbox"{idattr}>
            <left>{left}</left><top>{top}</top><width>{width}</width><height>{height}</height>
            <font>{font}</font><textcolor>{color}</textcolor><align>left</align>{lab}{sc}
        </control>"""

def img(left, top, width, height, tex, diffuse, border=None):
    b = f' border="{border}"' if border else ""
    return f"""
        <control type="image">
            <left>{left}</left><top>{top}</top><width>{width}</width><height>{height}</height>
            <texture{b} colordiffuse="{diffuse}">{tex}</texture>
        </control>"""

SHADE = """
        <control type="image">
            <width>1920</width><height>1080</height>
            <texture>common/modern-shade.png</texture>
        </control>"""

ANIM = "\n        <include>Animation.Common</include>"

def header(title, crumb="$LOCALIZE[5]"):
    return lbl(96, 92, 1200, 34, "ModernSmall", MUTED, crumb) + lbl(96, 124, 1300, 84, "ModernTitle", TXT, title)

# ------------------------------------------------------------ Einstellungs-Zeilen (Templates 7-15)
def templates(width, rowh, font, offx, nofocus=None, radio_right=24):
    nf = f'<texturenofocus border="14" colordiffuse="{nofocus}">common/modern-round14.png</texturenofocus>' if nofocus else "<texturenofocus />"
    common = f"""
            <width>{width}</width>
            <height>{rowh}</height>
            <font>{font}</font>
            <textoffsetx>{offx}</textoffsetx>
            <align>left</align>
            <aligny>center</aligny>
            <textcolor>{TXT}</textcolor>
            <focusedcolor>{DARK}</focusedcolor>
            <disabledcolor>{DIS}</disabledcolor>
            <texturefocus border="14" colordiffuse="{W}">common/modern-round14.png</texturefocus>
            {nf}"""
    spin = f"""
            <textureup colordiffuse="00ffffff">buttons/spin-down.png</textureup>
            <texturedown colordiffuse="00ffffff">buttons/spin-down.png</texturedown>
            <textureupfocus flipy="true" colordiffuse="{DARK}">buttons/spin-down.png</textureupfocus>
            <texturedownfocus colordiffuse="{DARK}">buttons/spin-down.png</texturedownfocus>
            <textureupdisabled colordiffuse="00ffffff">buttons/spin-down.png</textureupdisabled>
            <texturedowndisabled colordiffuse="00ffffff">buttons/spin-down.png</texturedowndisabled>
            <spinwidth>28</spinwidth><spinheight>28</spinheight>"""
    rx = width - radio_right - 56
    radio = f"""
            <radioposx>{rx}</radioposx>
            <radiowidth>56</radiowidth>
            <radioheight>32</radioheight>
            <textureradioonfocus>buttons/modern-switch-on-focus.png</textureradioonfocus>
            <textureradioonnofocus>buttons/modern-switch-on.png</textureradioonnofocus>
            <textureradioofffocus>buttons/modern-switch-off-focus.png</textureradioofffocus>
            <textureradiooffnofocus>buttons/modern-switch-off.png</textureradiooffnofocus>
            <textureradioondisabled colordiffuse="59ffffff">buttons/modern-switch-on.png</textureradioondisabled>
            <textureradiooffdisabled colordiffuse="59ffffff">buttons/modern-switch-off.png</textureradiooffdisabled>"""
    slider = f"""
            <sliderwidth>220</sliderwidth>
            <sliderheight>20</sliderheight>
            <texturesliderbar colordiffuse="66808890" border="3">osd/modern/bar.png</texturesliderbar>
            <textureslidernib>osd/modern/knob.png</textureslidernib>
            <textureslidernibfocus colordiffuse="{DARK}">osd/modern/knob.png</textureslidernibfocus>"""
    return f"""
    <control type="button" id="7">
        <description>Default Button</description>{common}
    </control>
    <control type="radiobutton" id="8">
        <description>Default Radio Button</description>{common}{radio}
    </control>
    <control type="spincontrolex" id="9">
        <description>Default Spin Control</description>{common}{spin}
    </control>
    <control type="edit" id="12">
        <description>Default Edit</description>{common}
    </control>
    <control type="sliderex" id="13">
        <description>Default Slider</description>{common}{slider}
    </control>
    <control type="colorbutton" id="15">
        <description>Default ColorButton</description>{common}
    </control>
    <control type="label" id="14">
        <description>Group Title</description>
        <width>{width}</width>
        <height>{int(rowh * 0.85)}</height>
        <font>ModernCaption</font>
        <textoffsetx>{offx}</textoffsetx>
        <aligny>center</aligny>
        <textcolor>{ACC}</textcolor>
    </control>"""

def category_button(width, height, font, offx, color, nofocus=None, sel="1fffffff", tex="common/modern-round14.png", border=14):
    w = f'<width min="80" max="420">auto</width>' if width == "auto" else f"<width>{width}</width>"
    nf = f'<texturenofocus border="{border}" colordiffuse="{nofocus}">{tex}</texturenofocus>' if nofocus else "<texturenofocus />"
    anf = f'<alttexturenofocus border="{border}" colordiffuse="{sel}">{tex}</alttexturenofocus>'
    return f"""
    <control type="togglebutton" id="10">
        <description>Default Category Button</description>
        {w}
        <height>{height}</height>
        <font>{font}</font>
        <textoffsetx>{offx}</textoffsetx>
        <align>{'center' if width == 'auto' else 'left'}</align>
        <aligny>center</aligny>
        <textcolor>{color}</textcolor>
        <focusedcolor>{DARK}</focusedcolor>
        <texturefocus border="{border}" colordiffuse="{W}">{tex}</texturefocus>
        {nf}
        <alttexturefocus border="{border}" colordiffuse="{W}">{tex}</alttexturefocus>
        {anf}
    </control>"""

def level_button(left, top, width=320):
    return lbl(left, top, width, 28, "ModernCaption", DIM, "$LOCALIZE[32106]") + f"""
        <control type="button" id="20">
            <left>{left}</left><top>{top + 30}</top>
            <width min="120" max="{width}">auto</width><height>44</height>
            <font>ModernSmall</font><textoffsetx>18</textoffsetx><align>left</align><aligny>center</aligny>
            <textcolor>{TXT}</textcolor><focusedcolor>{DARK}</focusedcolor>
            <texturefocus border="27" colordiffuse="{W}">common/modern-pill.png</texturefocus>
            <texturenofocus border="27" colordiffuse="14ffffff">common/modern-pill.png</texturenofocus>
            <onclick>SettingsLevelChange</onclick>
            <onup>3</onup><ondown>3</ondown><onright>3</onright><onleft>noop</onleft>
        </control>"""

def grouplist(cid, left, top, width, height, orient="vertical", gap=4, nav=""):
    return f"""
        <control type="grouplist" id="{cid}">
            <left>{left}</left><top>{top}</top><width>{width}</width><height>{height}</height>
            <orientation>{orient}</orientation><itemgap>{gap}</itemgap>
            <scrolltime tween="cubic" easing="out">200</scrolltime>
            {nav}
        </control>"""

# ------------------------------------------------------------ Kategorie-Seiten
cat_a = f"""
    <include name="SettingsCat_A">
    <control type="group">{ANIM}{SHADE}
        {header("$VAR[Label_SettingsHeader]")}
        {grouplist(3, 96, 290, 340, 620, gap=6, nav="<onright>5</onright><onleft>20</onleft><onup>3</onup><ondown>3</ondown>")}
        {grouplist(5, 480, 270, 1344, 660, nav="<onleft>3</onleft><onup>5</onup><ondown>5</ondown>")}
        {tbox(508, 950, 880, 72, "ModernSmall", MUTED, None, 6)}
        {level_button(96, 946)}
    </control>
    {category_button(340, 60, "ModernItem", 24, "ff8a929c")}
    {templates(1344, 72, "ModernRow", 28)}
    </include>
"""

cat_b = f"""
    <include name="SettingsCat_B">
    <control type="group">{ANIM}{SHADE}
        {lbl(96, 92, 900, 34, "ModernSmall", MUTED, "$LOCALIZE[5]  ·  $VAR[Label_SettingsHeader]")}
        {tbox(96, 140, 880, 170, "ModernH2", TXT, "$INFO[System.CurrentControl]", auto=False)}
        {tbox(96, 330, 880, 480, "ModernItem", MUTED, None, 6)}
        {level_button(96, 900)}
        <control type="group">
            <left>1060</left>
            <animation effect="slide" start="860,0" end="0,0" time="260" tween="cubic" easing="out">WindowOpen</animation>
            <animation effect="slide" start="0,0" end="860,0" time="200" tween="cubic" easing="in">WindowClose</animation>
            {img(-40, 0, 40, 1080, "common/modern-shade.png", "99ffffff")}
            {img(0, 0, 860, 1080, "common/white.png", "f516191e")}
            {grouplist(3, 56, 66, 748, 64, "horizontal", 8, "<ondown>5</ondown><onleft>20</onleft><onup>noop</onup>")}
            {img(56, 146, 748, 1, "common/white.png", "1fffffff")}
            {grouplist(5, 56, 166, 748, 880, nav="<onup>3</onup><onleft>20</onleft>")}
        </control>
    </control>
    {category_button("auto", 56, "ModernTile", 22, "ff7d858f", None, "29ffffff", "common/modern-pill.png", 27)}
    {templates(748, 68, "ModernTile", 22)}
    </include>
"""

cat_c = f"""
    <include name="SettingsCat_C">
    <control type="group">{ANIM}{SHADE}
        {header("$VAR[Label_SettingsHeader]")}
        {grouplist(3, 96, 250, 1150, 56, "horizontal", 12, "<ondown>5</ondown><onleft>20</onleft><onup>noop</onup>")}
        {grouplist(5, 96, 340, 1080, 690, nav="<onup>3</onup><onleft>20</onleft><onright>noop</onright>")}
        {img(1260, 340, 564, 500, "common/modern-round20.png", "12ffffff", 20)}
        {lbl(1300, 372, 480, 30, "ModernCaption", ACC, "$LOCALIZE[32123]")}
        {tbox(1300, 408, 484, 100, "ModernCard", TXT, "$INFO[System.CurrentControl]", auto=False)}
        {tbox(1300, 516, 484, 220, "ModernSmall", MUTED, None, 6)}
        {level_button(1300, 748, 480)}
    </control>
    {category_button("auto", 52, "ModernTile", 26, "ff8a929c", "14ffffff", "38ffffff", "common/modern-pill.png", 26)}
    {templates(1080, 66, "ModernRow", 22, nofocus="0fffffff")}
    </include>
"""

# ------------------------------------------------------------ Uebersicht (Fenster 4)
def tile_layout(w, h, tw, th, icon, label_top, font, focused, sub=False, zoom=None, radius="common/modern-round14.png", border=14, bg="12ffffff", lab_h=44, wrap=False, cid="9100"):
    tag = "focusedlayout" if focused else "itemlayout"
    def part(on, vis):
        bgc = W if on else bg
        ic = DARK if on else "e6ffffff"
        tc = DARK if on else TXT
        sc = "ff4a5058" if on else MUTED
        v = f"\n            <visible>{vis}</visible>" if vis else ""
        z = f'\n            <animation effect="zoom" start="100" end="{zoom}" time="150" tween="cubic" easing="out" center="auto">Visible</animation>' if (zoom and on) else ""
        subl = f"""
            <control type="label">
                <left>{icon[0]}</left><top>{label_top + 46}</top><width>{tw - icon[0] - 20}</width><height>30</height>
                <font>ModernCaption</font><textcolor>{sc}</textcolor>
                <label>$INFO[ListItem.Property(Short)]</label>
            </control>""" if sub else ""
        wr = "<wrapmultiline>true</wrapmultiline>" if wrap else ""
        if on:
            wr = "<scroll>true</scroll><scrollspeed>50</scrollspeed>"
        return f"""
            <control type="group">{v}{z}
            <control type="image">
                <width>{tw}</width><height>{th}</height>
                <texture border="{border}" colordiffuse="{bgc}">{radius}</texture>
            </control>
            <control type="image">
                <left>{icon[0] - icon[2] // 4}</left><top>{icon[1] - icon[2] // 4}</top><width>{icon[2] * 3 // 2}</width><height>{icon[2] * 3 // 2}</height>
                <aspectratio>keep</aspectratio>
                <texture colordiffuse="{ic}">$INFO[ListItem.Icon]</texture>
            </control>
            <control type="label">
                <left>{icon[0]}</left><top>{label_top}</top><width>{tw - icon[0] - 16}</width><height>{lab_h}</height>
                <font>{font}</font><textcolor>{tc}</textcolor>{wr}
                <label>$INFO[ListItem.Label]</label>
            </control>{subl}
            </control>"""
    if focused:
        inner = part(True, f"Control.HasFocus({cid})") + part(False, f"!Control.HasFocus({cid})")
    else:
        inner = part(False, None)
    return f"""
        <{tag} width="{w}" height="{h}">{inner}
        </{tag}>"""

def list_row(w, h, focused):
    bgc = W if focused else "00ffffff"
    ic = DARK if focused else "ccffffff"
    tc = DARK if focused else TXT
    sc = "ff4a5058" if focused else DIM
    tag = "focusedlayout" if focused else "itemlayout"
    return f"""
        <{tag} width="{w}" height="{h}">
            <control type="image">
                <width>{w}</width><height>{h - 4}</height>
                <texture border="14" colordiffuse="{bgc}">common/modern-round14.png</texture>
            </control>
            <control type="image">
                <left>16</left><top>{(h - 4 - 52) // 2}</top><width>52</width><height>52</height>
                <aspectratio>keep</aspectratio>
                <texture colordiffuse="{ic}">$INFO[ListItem.Icon]</texture>
            </control>
            <control type="label">
                <left>84</left><top>4</top><width>{w - 100}</width><height>36</height>
                <font>ModernRow</font><textcolor>{tc}</textcolor>
                <label>$INFO[ListItem.Label]</label>
            </control>
            <control type="label">
                <left>84</left><top>38</top><width>{w - 100}</width><height>28</height>
                <font>ModernCaption</font><textcolor>{sc}</textcolor>
                <label>$INFO[ListItem.Property(Short)]</label>
            </control>
        </{tag}>"""

hub_a = f"""
    <include name="SettingsHub_A">
    <control type="group">{ANIM}{SHADE}
        {header("$LOCALIZE[32105]")}
        <control type="panel" id="9100">
            <left>96</left><top>300</top><width>1216</width><height>600</height>
            <orientation>vertical</orientation>
            <scrolltime tween="cubic" easing="out">200</scrolltime>
            <onright>noop</onright>
            {tile_layout(304, 196, 280, 172, (26, 24, 48), 112, "ModernTile", False)}
            {tile_layout(304, 196, 280, 172, (26, 24, 48), 112, "ModernTile", True, zoom=104)}
            <content><include>SettingsItemsModern</include></content>
        </control>
        {tbox(1380, 300, 444, 580, "ModernRow", MUTED, "$INFO[Container(9100).ListItem.Label2]", auto=False)}
    </control>
    </include>
"""

hub_b = f"""
    <include name="SettingsHub_B">
    <control type="group">{ANIM}{SHADE}
        {lbl(96, 96, 1200, 84, "ModernTitle", TXT, "$LOCALIZE[5]")}
        <control type="list" id="9100">
            <left>96</left><top>226</top><width>760</width><height>792</height>
            <orientation>vertical</orientation>
            <scrolltime tween="cubic" easing="out">200</scrolltime>
            <onright>noop</onright>
            {list_row(760, 72, False)}
            {list_row(760, 72, True)}
            <content><include>SettingsItemsModern</include></content>
        </control>
        {img(1000, 226, 824, 700, "common/modern-round20.png", "0fffffff", 20)}
        <control type="image">
            <left>1056</left><top>282</top><width>96</width><height>96</height>
            <aspectratio align="left">keep</aspectratio>
            <texture>$INFO[Container(9100).ListItem.Icon]</texture>
        </control>
        {tbox(1056, 410, 712, 480, "ModernItem", MUTED, "$INFO[Container(9100).ListItem.Label2]", auto=False)}
    </control>
    </include>
"""

hub_c = f"""
    <include name="SettingsHub_C">
    <control type="group">{ANIM}{SHADE}
        {lbl(96, 96, 1200, 84, "ModernTitle", TXT, "$LOCALIZE[5]")}
        {lbl(96, 246, 800, 36, "ModernTile", MUTED, "$LOCALIZE[32107]")}
        <control type="list" id="9100">
            <left>96</left><top>296</top><width>1760</width><height>290</height>
            <orientation>horizontal</orientation>
            <scrolltime tween="cubic" easing="out">200</scrolltime>
            <ondown>9101</ondown><onup>noop</onup>
            {tile_layout(426, 290, 400, 256, (34, 34, 60), 150, "ModernCard", False, sub=True, radius="common/modern-round20.png", border=20, bg="1fffffff")}
            {tile_layout(426, 290, 400, 256, (34, 34, 60), 150, "ModernCard", True, sub=True, zoom=105, radius="common/modern-round20.png", border=20)}
            <content><include>SettingsItemsTop</include></content>
        </control>
        {lbl(96, 626, 800, 36, "ModernTile", MUTED, "$LOCALIZE[32108]")}
        <control type="list" id="9101">
            <left>96</left><top>676</top><width>1760</width><height>200</height>
            <orientation>horizontal</orientation>
            <scrolltime tween="cubic" easing="out">200</scrolltime>
            <onup>9100</onup><ondown>noop</ondown>
            {tile_layout(214, 200, 196, 172, (22, 22, 40), 104, "ModernCaption", False, lab_h=40)}
            {tile_layout(214, 200, 196, 172, (22, 22, 40), 104, "ModernCaption", True, zoom=105, lab_h=40, cid="9101")}
            <content><include>SettingsItemsRest</include></content>
        </control>
    </control>
    </include>
"""

xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- Arctic Zephyr - Modern: Einstellungs-Designs A/B/C.
     Generiert von tools/gen_settings_modern.py - bitte dort aendern. -->
<includes>
    <include name="SettingsItemsModern">
{items_modern}
    </include>
    <include name="SettingsItemsTop">
{items_top}
    </include>
    <include name="SettingsItemsRest">
{items_rest}
    </include>
{hub_a}
{hub_b}
{hub_c}
{cat_a}
{cat_b}
{cat_c}
</includes>
"""
open(OUT, "w", encoding="utf-8").write(xml)
print("geschrieben:", OUT, len(xml))
