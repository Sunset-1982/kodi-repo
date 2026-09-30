#!/usr/bin/env python3
"""Erzeugt DialogContextMenu.xml und DialogButtonMenu.xml (Powermenue) im Modern-Stil (Variante A: Karte).
Aufruf im Skin-Ordner: python3 ../tools/gen_menus_modern.py"""
import sys
SKIN = sys.argv[1] if len(sys.argv) > 1 else "."
TXT, MUTED = "ffececec", "ff98a0aa"
W, DARK = "$VAR[ModernFocus]", "$VAR[ModernFocusText]"
BG = "$VAR[ModernBg]"
CARD_W = 560          # Kartenbreite (sichtbar)
PAD = 28              # Schattenrand der Textur modern-card.png
ROW = 60              # Zeilenhoehe
INSET = 14            # Abstand der Fokusflaeche zum Kartenrand
HEAD = 118            # Hoehe Kopfbereich

def header(caption, title):
    return f"""
            <control type="label">
                <left>34</left><top>24</top><width>{CARD_W - 68}</width><height>28</height>
                <font>ModernCaption</font><textcolor>{MUTED}</textcolor>
                <label>{caption}</label>
            </control>
            <control type="label">
                <left>34</left><top>50</top><width>{CARD_W - 68}</width><height>46</height>
                <font>ModernCard</font><textcolor>{TXT}</textcolor>
                <label>{title}</label>
            </control>
            <control type="image">
                <left>24</left><top>{HEAD - 12}</top><width>{CARD_W - 48}</width><height>1</height>
                <texture colordiffuse="14ffffff">common/white.png</texture>
            </control>"""

DIM = """
        <control type="image">
            <width>1920</width><height>1080</height>
            <texture colordiffuse="99000000">common/white.png</texture>
            <animation effect="fade" start="0" end="100" time="150">WindowOpen</animation>
            <animation effect="fade" start="100" end="0" time="150">WindowClose</animation>
        </control>"""

ANIM = """
            <animation type="WindowOpen" reversible="false">
                <effect type="fade" start="0" end="100" time="160"/>
                <effect type="zoom" start="96" end="100" time="200" tween="cubic" easing="out" center="960,540"/>
            </animation>
            <animation type="WindowClose" reversible="false">
                <effect type="fade" start="100" end="0" time="120"/>
            </animation>"""

# ------------------------------------------------------------------ Kontextmenue
context = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- Arctic Zephyr - Modern: Kontextmenue als abgerundete Karte. Generiert von tools/gen_menus_modern.py -->
<window id="106">
    <defaultcontrol always="true">1000</defaultcontrol>
    <coordinates>
        <origin x="0" y="0"/>
    </coordinates>
    <controls>{DIM}
        <control type="group">{ANIM}
            <top>170</top>
            <centerleft>50%</centerleft>
            <width>{CARD_W}</width>
            <control type="image" id="999">
                <description>Hintergrund (Kodi: Hoehe = XML-Hoehe - 700 + Inhalt der Liste 996)</description>
                <left>-{PAD}</left><top>-{PAD}</top><width>{CARD_W + 2 * PAD}</width><height>{HEAD + 700 + 14 + 2 * PAD}</height>
                <texture border="{PAD + 24}" colordiffuse="{BG}">common/modern-card.png</texture>
            </control>
            {header("$VAR[ModernContextCaption]", "$VAR[ModernContextTitle]")}
            <control type="group">
                <visible>Container(996).HasNext | Container(996).HasPrevious</visible>
                <control type="image">
                    <centerleft>50%</centerleft><top>-40</top><width>32</width><height>16</height>
                    <texture colordiffuse="99ffffff" flipy="true">common/arrow-small.png</texture>
                </control>
            </control>
            <control type="grouplist" id="996">
                <description>grouplist for context buttons</description>
                <top>{HEAD}</top>
                <left>{INSET}</left>
                <right>{INSET}</right>
                <height max="700">auto</height>
                <itemgap>2</itemgap>
                <scrolltime tween="cubic" easing="out">150</scrolltime>
                <control type="button" id="1000">
                    <description>Buttons</description>
                    <height>{ROW}</height>
                    <font>ModernTile</font>
                    <textoffsetx>20</textoffsetx>
                    <align>left</align>
                    <aligny>center</aligny>
                    <textcolor>{TXT}</textcolor>
                    <focusedcolor>{DARK}</focusedcolor>
                    <texturefocus border="14" colordiffuse="{W}">common/modern-round14.png</texturefocus>
                    <texturenofocus />
                    <alttexturefocus border="14" colordiffuse="{W}">common/modern-round14.png</alttexturefocus>
                    <alttexturenofocus />
                </control>
            </control>
        </control>
    </controls>
</window>
"""

# ------------------------------------------------------------------ Powermenue
PM_ICONS = [("cancelalarm", "timeroff"), ("alarmclock", "timer"), ("shutdowntimer", "timer"), ("reloadskin", "reload"), ("quit", "exit"), ("powerdown", "power"), ("shutdown", "power"),
            ("suspend", "moon"), ("hibernate", "moon"), ("reboottoandroid", "chip"), ("rebootto", "chip"), ("emmc", "chip"),
            ("reset", "reboot"), ("reboot", "reboot"), ("restart", "reboot"), ("logoff", "logout"), ("mastermode", "lock"),
            ("inhibitidleshutdown", "eye"), ("cancelalarm", "timeroff"), ("alarmclock", "timer"), ("settings", "settings")]
icon_var = '    <variable name="ModernPowerIcon">\n' + "".join(
    f'        <value condition="String.Contains(ListItem.Property(path),{k})">osd/modern/pm-{g}.png</value>\n' for k, g in PM_ICONS
) + '        <value>osd/modern/pm-dot.png</value>\n    </variable>\n'

def pm_bg(n):
    h = HEAD + n * (ROW + 2) + 14 + 2 * PAD
    cond = f"Integer.IsEqual(Container(3110).NumItems,{n})" if n < 10 else "Integer.IsGreater(Container(3110).NumItems,9)"
    return f"""
            <control type="image">
                <left>-{PAD}</left><top>-{PAD}</top><width>{CARD_W + 2 * PAD}</width><height>{h}</height>
                <texture border="{PAD + 24}" colordiffuse="{BG}">common/modern-card.png</texture>
                <visible>{cond}</visible>
            </control>"""

def pm_row(focused):
    tag = "focusedlayout" if focused else "itemlayout"
    fill = f"""
                    <control type="image">
                        <width>{CARD_W - 2 * INSET}</width><height>{ROW}</height>
                        <texture border="14" colordiffuse="{W}">common/modern-round14.png</texture>
                        <visible>Control.HasFocus(3110)</visible>
                    </control>""" if focused else ""
    c = f"$VAR[ModernPowerRowColor]" if focused else TXT
    ic = f"$VAR[ModernPowerRowColor]" if focused else "ccffffff"
    return f"""
                <{tag} width="{CARD_W - 2 * INSET}" height="{ROW + 2}">{fill}
                    <control type="image">
                        <left>20</left><top>{(ROW - 30) // 2}</top><width>30</width><height>30</height>
                        <texture colordiffuse="{ic}">$VAR[ModernPowerIcon]</texture>
                    </control>
                    <control type="label">
                        <left>66</left><width>{CARD_W - 2 * INSET - 86}</width><height>{ROW}</height>
                        <aligny>center</aligny>
                        <font>ModernTile</font><textcolor>{c}</textcolor>
                        <label>$INFO[ListItem.Label]</label>
                    </control>
                </{tag}>"""

power = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- Arctic Zephyr - Modern: Powermenue als abgerundete Karte mit Symbolen. Generiert von tools/gen_menus_modern.py -->
<window type="buttonMenu" id="111">
    <defaultcontrol always="true">3110</defaultcontrol>
    <zorder>10</zorder>
    <controls>{DIM}
        <control type="group">{ANIM}
            <top>170</top>
            <centerleft>50%</centerleft>
            <width>{CARD_W}</width>
            {''.join(pm_bg(n) for n in range(1, 11))}
            {header("$INFO[System.Date]", "$LOCALIZE[31151]")}
            <control type="label">
                <right>34</right><top>24</top><width>200</width><height>28</height><align>right</align>
                <font>ModernCaption</font><textcolor>{MUTED}</textcolor>
                <label>$INFO[System.Time]</label>
            </control>
            <control type="list" id="3110">
                <top>{HEAD}</top>
                <left>{INSET}</left>
                <width>{CARD_W - 2 * INSET}</width>
                <height min="{ROW}" max="{9 * (ROW + 2)}">auto</height>
                <onup>3110</onup>
                <ondown>3110</ondown>
                <onleft>Close</onleft>
                <onright>Close</onright>
                <onback>300</onback>
                <orientation>vertical</orientation>
                <scrolltime tween="cubic" easing="out">150</scrolltime>
                {pm_row(False)}
                {pm_row(True)}
                <content>
                    <include>skinshortcuts-group-powermenu</include>
                </content>
            </control>
        </control>
    </controls>
</window>
"""

variables = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- Arctic Zephyr - Modern: Variablen fuer Kontext- und Powermenue. Generiert von tools/gen_menus_modern.py -->
<includes>
    <variable name="ModernContextCaption">
        <value condition="String.IsEqual(ListItem.DBType,movie)">$LOCALIZE[20338]</value>
        <value condition="String.IsEqual(ListItem.DBType,tvshow)">$LOCALIZE[20364]</value>
        <value condition="String.IsEqual(ListItem.DBType,season)">$LOCALIZE[20373]</value>
        <value condition="String.IsEqual(ListItem.DBType,episode)">$LOCALIZE[20359]</value>
        <value condition="String.IsEqual(ListItem.DBType,musicvideo)">$LOCALIZE[20391]</value>
        <value condition="String.IsEqual(ListItem.DBType,artist)">$LOCALIZE[557]</value>
        <value condition="String.IsEqual(ListItem.DBType,album)">$LOCALIZE[558]</value>
        <value condition="String.IsEqual(ListItem.DBType,song)">$LOCALIZE[179]</value>
        <value condition="!String.IsEmpty(ListItem.Label)">$LOCALIZE[10106]</value>
    </variable>
    <variable name="ModernContextTitle">
        <value condition="String.IsEqual(ListItem.DBType,episode) + !String.IsEmpty(ListItem.TVShowTitle)">$INFO[ListItem.TVShowTitle]: $INFO[ListItem.Title]</value>
        <value condition="!String.IsEmpty(ListItem.Label) + !String.IsEqual(ListItem.Label,..)">$INFO[ListItem.Label]</value>
        <value>$LOCALIZE[10106]</value>
    </variable>
    <variable name="ModernPowerRowColor">
        <value condition="Control.HasFocus(3110)">{DARK}</value>
        <value>{TXT}</value>
    </variable>
    <variable name="ModernFileText20">
        <value condition="Control.HasFocus(20)">{DARK}</value>
        <value>{TXT}</value>
    </variable>
    <variable name="ModernFileText21">
        <value condition="Control.HasFocus(21)">{DARK}</value>
        <value>{TXT}</value>
    </variable>
{icon_var}</includes>
"""

open(f"{SKIN}/1080i/DialogContextMenu.xml", "w", encoding="utf-8").write(context)
open(f"{SKIN}/1080i/DialogButtonMenu.xml", "w", encoding="utf-8").write(power)
open(f"{SKIN}/1080i/Includes_MenusModern.xml", "w", encoding="utf-8").write(variables)
print("geschrieben: DialogContextMenu.xml, DialogButtonMenu.xml, Includes_MenusModern.xml")
