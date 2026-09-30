#!/usr/bin/env python3
"""Erzeugt 1080i/Includes_OSDModern.xml fuer Arctic Zephyr - Modern.
OSD-Varianten: Kino (Skin.String(OSDStyle) leer) und Kompakt (OSDStyle=kompakt).
"""
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "1080i/Includes_OSDModern.xml"

W = "fff1f3f5"      # Fokus-Weiss
DARK = "ff14171b"   # Text auf Weiss
TXT = "ffececec"
MUTED = "ffa8b0b9"
ACC = "ff9db0cf"

FULL = "[Window.IsVisible(videoosd) | Player.Paused | Window.IsVisible(fullscreeninfo) | Player.ShowInfo | !String.IsEmpty(Window(home).Property(osdinfo))]"

def x(s):
    return s

# ---------------------------------------------------------------- Variablen
variables = f"""
    <!-- ===== Modern OSD: Variablen ===== -->
    <variable name="ModernOSD_Title">
        <value condition="VideoPlayer.Content(episodes)">$INFO[VideoPlayer.TVShowTitle]</value>
        <value condition="!String.IsEmpty(VideoPlayer.Title)">$INFO[VideoPlayer.Title]</value>
        <value>$INFO[Player.Title]</value>
    </variable>
    <variable name="ModernOSD_Meta">
        <value condition="VideoPlayer.Content(episodes)">$INFO[VideoPlayer.Season,S,]$INFO[VideoPlayer.Episode,E,]$INFO[VideoPlayer.Title,  ·  ,]</value>
        <value>$INFO[VideoPlayer.Year]$INFO[VideoPlayer.Duration,  ·  ,]$INFO[VideoPlayer.Genre,  ·  ,]$INFO[VideoPlayer.mpaa,  ·  ,]</value>
    </variable>
    <variable name="ModernOSD_Resolution">
        <value condition="String.IsEqual(VideoPlayer.VideoResolution,4K) | String.IsEqual(VideoPlayer.VideoResolution,2160)">4K</value>
        <value condition="String.IsEqual(VideoPlayer.VideoResolution,1080)">1080p</value>
        <value condition="String.IsEqual(VideoPlayer.VideoResolution,720)">720p</value>
        <value condition="String.IsEqual(VideoPlayer.VideoResolution,8K) | String.IsEqual(VideoPlayer.VideoResolution,4320)">8K</value>
        <value>$INFO[VideoPlayer.VideoResolution]</value>
    </variable>
    <variable name="ModernOSD_HDR">
        <value condition="String.IsEqual(VideoPlayer.HdrType,dolbyvision)">Dolby Vision</value>
        <value condition="String.IsEqual(VideoPlayer.HdrType,hdr10plus)">HDR10+</value>
        <value condition="String.IsEqual(VideoPlayer.HdrType,hdr10)">HDR10</value>
        <value condition="String.IsEqual(VideoPlayer.HdrType,hlg)">HLG</value>
    </variable>
    <variable name="ModernOSD_AudioCodec">
        <value condition="String.Contains(VideoPlayer.AudioCodec,truehd)">TrueHD</value>
        <value condition="String.IsEqual(VideoPlayer.AudioCodec,eac3) | String.IsEqual(VideoPlayer.AudioCodec,eac3_ddp_atmos)">DD+</value>
        <value condition="String.IsEqual(VideoPlayer.AudioCodec,ac3)">Dolby Digital</value>
        <value condition="String.IsEqual(VideoPlayer.AudioCodec,dtshd_ma) | String.IsEqual(VideoPlayer.AudioCodec,dtshd_ma_x) | String.IsEqual(VideoPlayer.AudioCodec,dtshd_ma_x_imax)">DTS-HD MA</value>
        <value condition="String.IsEqual(VideoPlayer.AudioCodec,dtshd_hra)">DTS-HD HRA</value>
        <value condition="String.StartsWith(VideoPlayer.AudioCodec,dts) | String.IsEqual(VideoPlayer.AudioCodec,dca)">DTS</value>
        <value condition="String.IsEqual(VideoPlayer.AudioCodec,aac)">AAC</value>
        <value condition="String.IsEqual(VideoPlayer.AudioCodec,flac)">FLAC</value>
        <value condition="String.IsEqual(VideoPlayer.AudioCodec,opus)">Opus</value>
        <value condition="String.IsEqual(VideoPlayer.AudioCodec,mp3)">MP3</value>
        <value condition="String.StartsWith(VideoPlayer.AudioCodec,pcm)">PCM</value>
        <value>$INFO[VideoPlayer.AudioCodec]</value>
    </variable>
    <variable name="ModernOSD_AudioChannels">
        <value condition="String.IsEqual(VideoPlayer.AudioChannels,8)">7.1</value>
        <value condition="String.IsEqual(VideoPlayer.AudioChannels,7)">6.1</value>
        <value condition="String.IsEqual(VideoPlayer.AudioChannels,6)">5.1</value>
        <value condition="String.IsEqual(VideoPlayer.AudioChannels,2)">Stereo</value>
        <value condition="String.IsEqual(VideoPlayer.AudioChannels,1)">Mono</value>
        <value>$INFO[VideoPlayer.AudioChannels]</value>
    </variable>
    <variable name="ModernOSD_AudioLanguage">
        <value condition="String.IsEqual(VideoPlayer.AudioLanguage,ger) | String.IsEqual(VideoPlayer.AudioLanguage,deu) | String.IsEqual(VideoPlayer.AudioLanguage,de)">$LOCALIZE[32140]</value>
        <value condition="String.IsEqual(VideoPlayer.AudioLanguage,eng) | String.IsEqual(VideoPlayer.AudioLanguage,en)">$LOCALIZE[32141]</value>
        <value condition="String.IsEqual(VideoPlayer.AudioLanguage,fre) | String.IsEqual(VideoPlayer.AudioLanguage,fra)">$LOCALIZE[32142]</value>
        <value condition="String.IsEqual(VideoPlayer.AudioLanguage,spa)">$LOCALIZE[32143]</value>
        <value condition="String.IsEqual(VideoPlayer.AudioLanguage,ita)">$LOCALIZE[32144]</value>
        <value condition="String.IsEqual(VideoPlayer.AudioLanguage,jpn)">$LOCALIZE[32145]</value>
        <value condition="String.IsEqual(VideoPlayer.AudioLanguage,und) | String.IsEmpty(VideoPlayer.AudioLanguage)">$LOCALIZE[292]</value>
        <value>$INFO[VideoPlayer.AudioLanguage]</value>
    </variable>
    <variable name="ModernOSD_SubLanguage">
        <value condition="!VideoPlayer.SubtitlesEnabled">$LOCALIZE[32132]</value>
        <value condition="String.IsEqual(VideoPlayer.SubtitlesLanguage,ger) | String.IsEqual(VideoPlayer.SubtitlesLanguage,deu)">$LOCALIZE[32140]</value>
        <value condition="String.IsEqual(VideoPlayer.SubtitlesLanguage,eng)">$LOCALIZE[32141]</value>
        <value>$INFO[VideoPlayer.SubtitlesLanguage]</value>
    </variable>
    <variable name="ModernOSD_Poster">
        <value condition="!String.IsEmpty(Player.Art(tvshow.poster))">$INFO[Player.Art(tvshow.poster)]</value>
        <value condition="!String.IsEmpty(Player.Art(poster))">$INFO[Player.Art(poster)]</value>
        <value>$INFO[Player.Art(thumb)]</value>
    </variable>
    <variable name="ModernOSD_Time">
        <value condition="Player.Seeking + !String.IsEmpty(Player.SeekTime)">$INFO[Player.SeekTime]</value>
        <value>$INFO[Player.Time]</value>
    </variable>
"""

# ---------------------------------------------------------------- Bausteine
def chip(label, visible):
    return f"""
                <control type="button">
                    <width min="40" max="400">auto</width>
                    <height>32</height>
                    <font>ModernCaption</font>
                    <textoffsetx>12</textoffsetx>
                    <align>center</align>
                    <aligny>center</aligny>
                    <enable>false</enable>
                    <disabledcolor>ffe2e5e8</disabledcolor>
                    <texturenofocus border="9" colordiffuse="66ffffff">common/modern-chip.png</texturenofocus>
                    <texturefocus border="9" colordiffuse="66ffffff">common/modern-chip.png</texturefocus>
                    <label>{label}</label>
                    <visible>{visible}</visible>
                </control>"""

def chips(left, top, width):
    return f"""
            <control type="grouplist">
                <left>{left}</left>
                <top>{top}</top>
                <width>{width}</width>
                <height>32</height>
                <orientation>horizontal</orientation>
                <itemgap>10</itemgap>
                <usecontrolcoords>true</usecontrolcoords>
                {chip('$VAR[ModernOSD_Resolution]','!String.IsEmpty(VideoPlayer.VideoResolution)')}
                {chip('$VAR[ModernOSD_HDR]','!String.IsEmpty(VideoPlayer.HdrType)')}
                {chip('$VAR[ModernOSD_AudioCodec]$INFO[VideoPlayer.AudioChannels, ,]'.replace('$INFO[VideoPlayer.AudioChannels, ,]',' $VAR[ModernOSD_AudioChannels]'),'!String.IsEmpty(VideoPlayer.AudioCodec)')}
                {chip('$VAR[ModernOSD_AudioLanguage]','!String.IsEmpty(VideoPlayer.AudioLanguage) + !String.IsEqual(VideoPlayer.AudioLanguage,und)')}
            </control>"""

def progress(left, top, width, knob=False):
    kn = f"""
                <control type="progress">
                    <left>-10</left>
                    <top>-7</top>
                    <width>{width + 20}</width>
                    <height>20</height>
                    <info>Player.Progress</info>
                    <texturebg />
                    <lefttexture />
                    <midtexture colordiffuse="00ffffff">osd/modern/bar.png</midtexture>
                    <righttexture>osd/modern/knob.png</righttexture>
                    <visible>!Player.Seeking</visible>
                </control>""" if knob else ""
    return f"""
            <control type="group">
                <left>{left}</left>
                <top>{top}</top>
                <width>{width}</width>
                <height>6</height>
                <control type="progress">
                    <width>{width}</width>
                    <height>6</height>
                    <info>Player.ProgressCache</info>
                    <texturebg border="3" colordiffuse="38ffffff">osd/modern/bar.png</texturebg>
                    <lefttexture />
                    <midtexture border="3" colordiffuse="40ffffff">osd/modern/bar.png</midtexture>
                    <righttexture />
                </control>
                <control type="progress">
                    <width>{width}</width>
                    <height>6</height>
                    <info>Player.Progress</info>
                    <texturebg />
                    <lefttexture />
                    <midtexture border="3" colordiffuse="{W}">osd/modern/bar.png</midtexture>
                    <righttexture />
                    <visible>!Player.Seeking</visible>
                </control>
                <control type="progress" id="401">
                    <width>{width}</width>
                    <height>6</height>
                    <texturebg />
                    <lefttexture />
                    <midtexture border="3" colordiffuse="{W}">osd/modern/bar.png</midtexture>
                    <righttexture />
                    <visible>Player.Seeking</visible>
                </control>
                <control type="ranges">
                    <top>-4</top>
                    <width>{width}</width>
                    <height>12</height>
                    <texturebg />
                    <lefttexture />
                    <midtexture />
                    <righttexture colordiffuse="aa000000">osd/modern/tick.png</righttexture>
                    <info>Player.Chapters</info>
                </control>{kn}
            </control>"""

def bubble(left, top, width):
    """Zeit-Blase, die ueber gestaffelte Slide-Animationen dem Fortschritt folgt."""
    step = width / 100.0
    anims = "\n".join(
        f'                <animation effect="slide" end="{step:.2f},0" time="0" condition="Integer.IsGreaterOrEqual(Player.Progress,{i})">Conditional</animation>'
        for i in range(1, 101))
    return f"""
            <control type="group">
                <left>{left - 100}</left>
                <top>{top}</top>
                <width>200</width>
                <height>70</height>
{anims}
                <control type="image">
                    <width>200</width>
                    <height>70</height>
                    <texture border="14" colordiffuse="{W}">common/modern-round14.png</texture>
                </control>
                <control type="label">
                    <top>6</top>
                    <width>200</width>
                    <height>36</height>
                    <align>center</align>
                    <font>ModernRowBold</font>
                    <textcolor>{DARK}</textcolor>
                    <label>$VAR[ModernOSD_Time]</label>
                </control>
                <control type="label">
                    <top>38</top>
                    <width>200</width>
                    <height>26</height>
                    <align>center</align>
                    <font>ModernCaption</font>
                    <textcolor>ff555c64</textcolor>
                    <label>$INFO[Player.SeekOffset]</label>
                </control>
            </control>"""

def minimal_seek():
    return f"""
        <!-- Nur Spulen / Springen: schlanke Leiste mit Zeit-Blase -->
        <control type="group">
            <visible>!{FULL}</visible>
            <animation effect="fade" start="0" end="100" time="150">Visible</animation>
            <animation effect="fade" start="100" end="0" time="200">Hidden</animation>
            <control type="image">
                <top>680</top>
                <width>1920</width>
                <height>400</height>
                <texture colordiffuse="b3ffffff">osd/modern/shade-bottom.png</texture>
            </control>
            {bubble(96, 880, 1728)}
            {progress(96, 964, 1728)}
            <control type="label">
                <left>96</left>
                <top>986</top>
                <width>1000</width>
                <height>34</height>
                <font>ModernSmall</font>
                <textcolor>{MUTED}</textcolor>
                <label>$INFO[Player.ChapterName]</label>
            </control>
            <control type="label">
                <right>96</right>
                <top>986</top>
                <width>400</width>
                <height>34</height>
                <align>right</align>
                <font>ModernSmall</font>
                <textcolor>{MUTED}</textcolor>
                <label>$INFO[Player.TimeRemaining,−,]</label>
            </control>
        </control>"""

def clock(right, top, font="ClockModern", sub_top=None):
    sub_top = sub_top if sub_top is not None else top + 76
    return f"""
            <control type="label">
                <right>{right}</right>
                <top>{top}</top>
                <width>400</width>
                <height>70</height>
                <align>right</align>
                <font>{font}</font>
                <textcolor>{TXT}</textcolor>
                <label>$INFO[System.Time(hh:mm)]</label>
            </control>
            <control type="label">
                <right>{right}</right>
                <top>{sub_top}</top>
                <width>400</width>
                <height>32</height>
                <align>right</align>
                <font>ModernSmall</font>
                <textcolor>{MUTED}</textcolor>
                <label>$LOCALIZE[32130] $INFO[Player.FinishTime]</label>
                <visible>!String.IsEmpty(Player.FinishTime)</visible>
            </control>"""

# ---------------------------------------------------------------- Seekbar Kino
seek_kino = f"""
    <include name="SeekbarKino">
        <control type="group">
            <visible>{FULL}</visible>
            <animation effect="fade" start="0" end="100" time="200">Visible</animation>
            <animation effect="fade" start="100" end="0" time="200">Hidden</animation>
            <animation effect="fade" start="100" end="0" time="150" condition="Window.IsVisible(DialogPlayerProcessInfo.xml) | Window.IsVisible(osdaudiosettings) | Window.IsVisible(osdvideosettings) | Window.IsVisible(osdsubtitlesettings) | Window.IsVisible(videobookmarks)">Conditional</animation>
            <control type="image">
                <width>1920</width>
                <height>380</height>
                <texture colordiffuse="d9ffffff">osd/modern/shade-top.png</texture>
            </control>
            <control type="image">
                <top>500</top>
                <width>1920</width>
                <height>580</height>
                <texture>osd/modern/shade-bottom.png</texture>
            </control>
            <!-- Titel / Clearlogo -->
            <control type="image">
                <left>96</left>
                <top>64</top>
                <width>620</width>
                <height>150</height>
                <aspectratio align="left" aligny="bottom">keep</aspectratio>
                <texture>$INFO[Player.Art(clearlogo)]</texture>
                <visible>!String.IsEmpty(Player.Art(clearlogo))</visible>
            </control>
            <control type="label">
                <left>96</left>
                <top>120</top>
                <width>1300</width>
                <height>90</height>
                <aligny>bottom</aligny>
                <font>ModernTitle</font>
                <textcolor>{TXT}</textcolor>
                <label>$VAR[ModernOSD_Title]</label>
                <visible>String.IsEmpty(Player.Art(clearlogo))</visible>
            </control>
            <control type="label">
                <left>96</left>
                <top>226</top>
                <width>1300</width>
                <height>36</height>
                <font>ModernRow</font>
                <textcolor>{MUTED}</textcolor>
                <label>$VAR[ModernOSD_Meta]</label>
            </control>
            {chips(96, 276, 1300)}
            {clock(96, 64)}
            <!-- Kapitel + Status -->
            <control type="label">
                <left>96</left>
                <top>792</top>
                <width>900</width>
                <height>30</height>
                <font>ModernCaption</font>
                <textcolor>{ACC}</textcolor>
                <label>$LOCALIZE[21396] $INFO[Player.Chapter] / $INFO[Player.ChapterCount]</label>
                <visible>Integer.IsGreater(Player.ChapterCount,1)</visible>
            </control>
            <control type="label">
                <left>96</left>
                <top>822</top>
                <width>1200</width>
                <height>40</height>
                <font>ModernItem</font>
                <textcolor>{TXT}</textcolor>
                <label>$INFO[Player.ChapterName]</label>
            </control>
            <control type="label">
                <right>96</right>
                <top>826</top>
                <width>400</width>
                <height>34</height>
                <align>right</align>
                <font>ModernSmall</font>
                <textcolor>{MUTED}</textcolor>
                <label>$LOCALIZE[112]</label>
                <visible>Player.Paused</visible>
            </control>
            {progress(96, 876, 1728)}
            <control type="label">
                <left>96</left>
                <top>894</top>
                <width>600</width>
                <height>34</height>
                <font>ModernSmall</font>
                <textcolor>{TXT}</textcolor>
                <label>$VAR[ModernOSD_Time]</label>
            </control>
            <control type="label">
                <right>96</right>
                <top>894</top>
                <width>600</width>
                <height>34</height>
                <align>right</align>
                <font>ModernSmall</font>
                <textcolor>{MUTED}</textcolor>
                <label>$INFO[Player.TimeRemaining,−,]</label>
            </control>
        </control>
        {minimal_seek()}
    </include>
"""

# ---------------------------------------------------------------- Seekbar Kompakt
PANEL_T = 1080 - 64 - 300   # 716
seek_kompakt = f"""
    <include name="SeekbarKompakt">
        <control type="group">
            <visible>{FULL}</visible>
            <animation effect="fade" start="0" end="100" time="200">Visible</animation>
            <animation effect="fade" start="100" end="0" time="200">Hidden</animation>
            <animation effect="slide" start="0,40" end="0,0" time="220" tween="cubic" easing="out">Visible</animation>
            <animation effect="fade" start="100" end="0" time="150" condition="Window.IsVisible(DialogPlayerProcessInfo.xml) | Window.IsVisible(osdaudiosettings) | Window.IsVisible(osdvideosettings) | Window.IsVisible(osdsubtitlesettings) | Window.IsVisible(videobookmarks)">Conditional</animation>
            <control type="image">
                <top>600</top>
                <width>1920</width>
                <height>480</height>
                <texture colordiffuse="99ffffff">osd/modern/shade-bottom.png</texture>
            </control>
            <control type="image">
                <left>96</left>
                <top>{PANEL_T}</top>
                <width>1728</width>
                <height>300</height>
                <texture border="20" colordiffuse="e612151a">common/modern-round20.png</texture>
            </control>
            <control type="image">
                <left>128</left>
                <top>{PANEL_T + 32}</top>
                <width>158</width>
                <height>236</height>
                <aspectratio>scale</aspectratio>
                <texture diffuse="common/modern-round14.png">$VAR[ModernOSD_Poster]</texture>
            </control>
            <control type="label">
                <left>318</left>
                <top>{PANEL_T + 26}</top>
                <width>1100</width>
                <height>54</height>
                <font>ModernH2</font>
                <textcolor>{TXT}</textcolor>
                <label>$VAR[ModernOSD_Title]</label>
            </control>
            <control type="label">
                <left>318</left>
                <top>{PANEL_T + 82}</top>
                <width>1100</width>
                <height>32</height>
                <font>ModernSmall</font>
                <textcolor>{MUTED}</textcolor>
                <label>$VAR[ModernOSD_Meta]$INFO[Player.ChapterName,  ·  ,]</label>
            </control>
            {clock(128, PANEL_T + 26, "ModernH2", PANEL_T + 80)}
            {progress(318, PANEL_T + 142, 1474)}
            <control type="label">
                <left>318</left>
                <top>{PANEL_T + 160}</top>
                <width>600</width>
                <height>32</height>
                <font>ModernSmall</font>
                <textcolor>{TXT}</textcolor>
                <label>$VAR[ModernOSD_Time]</label>
            </control>
            <control type="label">
                <right>128</right>
                <top>{PANEL_T + 160}</top>
                <width>600</width>
                <height>32</height>
                <align>right</align>
                <font>ModernSmall</font>
                <textcolor>{MUTED}</textcolor>
                <label>$LOCALIZE[112]  ·  $INFO[Player.TimeRemaining,−,]</label>
                <visible>Player.Paused</visible>
            </control>
            <control type="label">
                <right>128</right>
                <top>{PANEL_T + 160}</top>
                <width>600</width>
                <height>32</height>
                <align>right</align>
                <font>ModernSmall</font>
                <textcolor>{MUTED}</textcolor>
                <label>$INFO[Player.TimeRemaining,−,]</label>
                <visible>!Player.Paused</visible>
            </control>
            {chips(318, PANEL_T + 226, 720)}
        </control>
        {minimal_seek()}
    </include>
"""

# ---------------------------------------------------------------- OSD-Buttons
def round_btn(cid, left, top, size, glyph, onclick, nav, visible=None, glyph_alt=None, extra=""):
    gs = int(size * 0.46)
    go = (size - gs) // 2
    vis = f"\n                <visible>{visible}</visible>" if visible else ""
    oc = "\n".join(f"                    <onclick>{o}</onclick>" for o in onclick) if isinstance(onclick, list) else f"                    <onclick>{onclick}</onclick>"
    def glyph_imgs(g, cond):
        c = f" + {cond}" if cond else ""
        return f"""
                <control type="image">
                    <left>{go}</left><top>{go}</top><width>{gs}</width><height>{gs}</height>
                    <texture colordiffuse="{DARK}">osd/modern/{g}.png</texture>
                    <visible>Control.HasFocus({cid}){c}</visible>
                </control>
                <control type="image">
                    <left>{go}</left><top>{go}</top><width>{gs}</width><height>{gs}</height>
                    <texture colordiffuse="{TXT}">osd/modern/{g}.png</texture>
                    <visible>!Control.HasFocus({cid}){c}</visible>
                </control>"""
    if glyph_alt:
        glyphs = glyph_imgs(glyph, "!Player.Paused") + glyph_imgs(glyph_alt, "Player.Paused")
    else:
        glyphs = glyph_imgs(glyph, None)
    return f"""
            <control type="group">
                <left>{left}</left>
                <top>{top}</top>
                <width>{size}</width>
                <height>{size}</height>{vis}
                <animation effect="zoom" start="100" end="108" center="auto" time="120" condition="Control.HasFocus({cid})">Conditional</animation>
                <control type="button" id="{cid}">
                    <width>{size}</width>
                    <height>{size}</height>
                    <label />
                    <texturefocus colordiffuse="{W}">osd/modern/circle.png</texturefocus>
                    <texturenofocus colordiffuse="26ffffff">osd/modern/circle.png</texturenofocus>
{oc}
                    {nav}{extra}
                </control>{glyphs}
            </control>"""

def pill(cid, label, onclick, visible=None, extra=""):
    vis = f"\n                    <visible>{visible}</visible>" if visible else ""
    oc = "\n".join(f"                    <onclick>{o}</onclick>" for o in onclick) if isinstance(onclick, list) else f"                    <onclick>{onclick}</onclick>"
    return f"""
                <control type="button" id="{cid}">
                    <width min="110" max="520">auto</width>
                    <height>56</height>
                    <font>ModernTile</font>
                    <textoffsetx>26</textoffsetx>
                    <align>center</align>
                    <aligny>center</aligny>
                    <textcolor>{TXT}</textcolor>
                    <focusedcolor>{DARK}</focusedcolor>
                    <texturefocus border="27" colordiffuse="{W}">common/modern-pill.png</texturefocus>
                    <texturenofocus border="27" colordiffuse="1fffffff">common/modern-pill.png</texturenofocus>
                    <label>{label}</label>
{oc}{vis}{extra}
                </control>"""

AUDIO = "ActivateWindow(osdaudiosettings)"
SUBS = "ActivateWindow(osdsubtitlesettings)"
VIDEO = "ActivateWindow(osdvideosettings)"
CHAP = "ActivateWindow(videobookmarks)"
PPI = "RunScript(script.signde.tinyppi,dialog)"
PPI_VIS = "System.HasAddon(script.signde.tinyppi)"
PPI_FALLBACK_VIS = "!System.HasAddon(script.signde.tinyppi)"

# Kino: Pillen links, runde Transport-Buttons mittig, Pillen rechts
cy = 1080 - 64 - 46          # Mittellinie 970
b, big, gap = 76, 92, 18
xs = []
x0 = 960 - (b * 5 + big + gap * 5) // 2
cur = x0
for i, s in enumerate([b, b, big, b, b, b]):
    xs.append((cur, s)); cur += s + gap
names = [("311", "prev", "PlayerControl(Previous)"), ("312", "rew", "PlayerControl(Rewind)"),
         ("313", "pause", "PlayerControl(Play)"), ("314", "ff", "PlayerControl(Forward)"),
         ("315", "next", "PlayerControl(Next)"), ("316", "stop", "PlayerControl(Stop)")]
kino_btns = ""
for i, ((cid, g, oc), (lx, s)) in enumerate(zip(names, xs)):
    left_id = "300" if i == 0 else names[i - 1][0]
    right_id = "320" if i == len(names) - 1 else names[i + 1][0]
    nav = f"<onleft>{left_id}</onleft>\n                    <onright>{right_id}</onright>\n                    <onup>noop</onup>\n                    <ondown>noop</ondown>"
    kino_btns += round_btn(cid, lx, cy - s // 2, s, g, oc, nav, glyph_alt="play" if g == "pause" else None)

osd_kino = f"""
    <include name="OSDKino">
        <control type="group">
            <animation type="WindowOpen"><effect type="fade" start="0" end="100" time="200"/></animation>
            <animation type="WindowClose"><effect type="fade" start="100" end="0" time="150"/></animation>
            <animation effect="fade" start="100" end="0" time="150" condition="Window.IsVisible(DialogPlayerProcessInfo.xml) | Window.IsVisible(osdaudiosettings) | Window.IsVisible(osdvideosettings) | Window.IsVisible(osdsubtitlesettings) | Window.IsVisible(videobookmarks)">Conditional</animation>
            <control type="grouplist" id="300">
                <left>96</left>
                <top>{cy - 28}</top>
                <width>{x0 - 96 - 30}</width>
                <height>56</height>
                <orientation>horizontal</orientation>
                <itemgap>12</itemgap>
                <onright>311</onright>
                <onleft>noop</onleft>
                <onup>noop</onup>
                <ondown>noop</ondown>
                <usecontrolcoords>true</usecontrolcoords>
                {pill("301", "$VAR[ModernOSD_AudioLanguage] $VAR[ModernOSD_AudioChannels]", AUDIO)}
                {pill("302", "$LOCALIZE[287]: $VAR[ModernOSD_SubLanguage]", SUBS)}
            </control>
            {kino_btns}
            <control type="grouplist" id="320">
                <right>96</right>
                <top>{cy - 28}</top>
                <width>{1920 - 96 - cur - 12}</width>
                <height>56</height>
                <orientation>horizontal</orientation>
                <align>right</align>
                <itemgap>12</itemgap>
                <onleft>316</onleft>
                <onright>noop</onright>
                <onup>noop</onup>
                <ondown>noop</ondown>
                <usecontrolcoords>true</usecontrolcoords>
                {pill("321", "$LOCALIZE[21396]", CHAP, "Integer.IsGreater(Player.ChapterCount,1)")}
                {pill("322", "$LOCALIZE[291]", VIDEO)}
                {pill("323", "$LOCALIZE[32133]", PPI, PPI_VIS)}
                {pill("325", "$LOCALIZE[32133]", "ActivateWindow(playerprocessinfo)", PPI_FALLBACK_VIS)}
                <control type="button" id="324">
                    <width min="110" max="520">auto</width>
                    <height>56</height>
                    <font>ModernTile</font>
                    <textoffsetx>26</textoffsetx>
                    <align>center</align>
                    <aligny>center</aligny>
                    <textcolor>{TXT}</textcolor>
                    <focusedcolor>{DARK}</focusedcolor>
                    <texturefocus border="27" colordiffuse="{W}">common/modern-pill.png</texturefocus>
                    <texturenofocus border="27" colordiffuse="1fffffff">common/modern-pill.png</texturenofocus>
                    <label>$LOCALIZE[32123]</label>
                    <include>OSDExtendedInfo_Click_Action</include>
                    <visible>VideoPlayer.Content(movies) | VideoPlayer.Content(episodes)</visible>
                </control>
            </control>
        </control>
    </include>
"""

# Kompakt: Icon-Buttons rechts im Panel
ks, kg = 68, 14
kbtns = [("501", "audio", AUDIO, None), ("502", "sub", SUBS, None), ("503", "rew", "PlayerControl(Rewind)", None),
         ("504", "pause", "PlayerControl(Play)", None), ("505", "ff", "PlayerControl(Forward)", None),
         ("506", "stop", "PlayerControl(Stop)", None), ("507", "chapters", CHAP, None),
         ("508", "ppi", PPI, PPI_VIS), ("510", "ppi", "ActivateWindow(playerprocessinfo)", PPI_FALLBACK_VIS),
         ("509", "info", None, "VideoPlayer.Content(movies) | VideoPlayer.Content(episodes)")]
# sichtbare Anzahl fuer Positionierung: 9 (eine der beiden PPI-Varianten)
visible_slots = [k for k in kbtns if k[0] != "510"]
right_edge = 96 + 1728 - 32
kx0 = right_edge - (len(visible_slots) * ks + (len(visible_slots) - 1) * kg)
ky = PANEL_T + 300 - 32 - ks
kompakt_btns = ""
slot = 0
ids_in_order = [k[0] for k in visible_slots]
for cid, g, oc, vis in kbtns:
    s = slot if cid != "510" else ids_in_order.index("508")
    lx = kx0 + s * (ks + kg)
    order = ids_in_order
    idx = order.index(cid) if cid in order else order.index("508")
    left_id = order[idx - 1] if idx > 0 else "noop"
    right_id = order[idx + 1] if idx < len(order) - 1 else "noop"
    # PPI-Nachbarn: beide Varianten bedienen
    if left_id == "508": left_id = "508"
    nav = f"<onleft>{left_id}</onleft>\n                    <onright>{right_id}</onright>\n                    <onup>noop</onup>\n                    <ondown>noop</ondown>"
    if cid == "509":
        onclick_xml = []
        extra = "\n                    <include>OSDExtendedInfo_Click_Action</include>"
        kompakt_btns += round_btn(cid, lx, ky, ks, g, [], nav, vis, None, extra).replace("\n\n", "\n")
    else:
        kompakt_btns += round_btn(cid, lx, ky, ks, g, oc, nav, vis, "play" if g == "pause" else None)
    if cid != "510":
        slot += 1

osd_kompakt = f"""
    <include name="OSDKompakt">
        <control type="group">
            <animation type="WindowOpen"><effect type="fade" start="0" end="100" time="200"/></animation>
            <animation type="WindowClose"><effect type="fade" start="100" end="0" time="150"/></animation>
            <animation effect="fade" start="100" end="0" time="150" condition="Window.IsVisible(DialogPlayerProcessInfo.xml) | Window.IsVisible(osdaudiosettings) | Window.IsVisible(osdvideosettings) | Window.IsVisible(osdsubtitlesettings) | Window.IsVisible(videobookmarks)">Conditional</animation>
            {kompakt_btns}
        </control>
    </include>
"""

xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- Arctic Zephyr - Modern: OSD-Varianten Kino und Kompakt.
     Generiert von tools/gen_osd_modern.py - bitte dort aendern. -->
<includes>
    <include name="OSDFocusKino">
        <defaultcontrol always="true">313</defaultcontrol>
    </include>
    <include name="OSDFocusKompakt">
        <defaultcontrol always="true">504</defaultcontrol>
    </include>
{variables}
{seek_kino}
{seek_kompakt}
{osd_kino}
{osd_kompakt}
</includes>
"""
open(OUT, "w", encoding="utf-8").write(xml)
print("geschrieben:", OUT, len(xml), "Zeichen")
