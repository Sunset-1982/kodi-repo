# Arctic Zephyr Modern: Änderungsprotokoll

**Add-on-ID:** `skin.arctic.zephyr.modern`, Name „Arctic: Zephyr - Modern“, Version 0.1.0 (Entscheidung vom 30.09.2026). Der Skin läuft parallel zum Original, und signde-Updates überschreiben ihn nicht.

Basis: `skin.arctic.zephyr.martian.signde` 11.3.20.2, Kodi 21.3.
Der Patch gegen das Original liegt unter `claude/patches/modern-01.patch` und betrifft `addon.xml` und die 1080i-XMLs. Anwenden mit `cd skin && patch -p1 < modern-01.patch`.

## Runde 1 (30.09.2026): Schrift, Versalien, Uhr, Fokusrahmen
1. **Schrift:** DM Sans (OFL, aus skin.bald) ist das neue Fontset „Default“. Die alte Roboto bleibt als „Classic (Roboto)“ wählbar.
   - Die Dateien `DMSans-Regular/Medium/SemiBold.ttf` und `DMSans-OFL.txt` aus skin.bald nach `fonts/` kopieren.
   - Roboto-Bold/Condensed-Bold → DMSans-SemiBold, Regular/Light → DMSans-Regular
   - `linespacing` im DM-Sans-Set immer **1.0**. Bruchwerte (0.9, 1.03, 1.05 …) lassen Textboxen wegen eines Rundungsfehlers scrollen, dann fehlt die erste Zeile der Beschreibung.
2. **Keine Versalien:** `<style>uppercase</style>` im Default-Set entfernt (Button, Flag, EPGTimeline, Home, HomeFO, HomeIcon, HomeLarge).
3. **Uhr:** In `Includes_Furniture.xml` (Furniture_Clock) nutzt die Uhr jetzt die Schrift `ClockModern` (DM Sans Regular 60, in allen Fontsets definiert) in `Dark1` statt ColorHighlight, `centertop` 18. „Clock“ gab es schon (Größe 130), deshalb der neue Name.
4. **Fokusrahmen:** `common/selectbox.png` (8 px, eckig) wurde durch `common/selectbox-modern.png` ersetzt (64×64, 3 px Ring, Radius 10, per PIL erzeugt). Die Farbe kommt aus der neuen Variable `ColorFocusFrame` (fff2f2f2). Die Verlaufsebene `gradient-selectbox*` ist über `ColorFocusGradient` = 00ffffff ausgeblendet. Die Variablen stehen in `Includes_Defs.xml`.

Offen / Ideen: Postertitel-Overlay und Flammen-Icons entfernen, Spiegelung weg, Medien-Flags als Text-Chips, Prozent-Ratings, Farben reduzieren, mehr Luft, Info-Dialog im Bald-Stil. Der Listen-Fokus in den Bibliotheksansichten ist noch ein hellgrauer Balken, in den Skin-Einstellungen ein blau-türkiser Verlaufsbalken.

## ID-Wechsel (Runde 1b)
- `addon.xml`: neue ID, Name und Version, provider-name um „a.sanns“ ergänzt, `<source>` (signde-GitHub) entfernt, eigener `<news>`-Block. Lizenz CC BY-NC-SA 3.0 und Credits bleiben erhalten.
- `SkinSettings.xml`: `System.AddonTitle/AddonVersion` zeigen auf die neue ID.

## Installation auf der Box (später)
Noch nicht bauen, das Projekt läuft weiter. Einstellungen übernehmen, damit Menüs und Widgets nicht neu eingerichtet werden müssen:
- `/storage/.kodi/userdata/addon_data/skin.arctic.zephyr.martian.signde/` → nach `…/skin.arctic.zephyr.modern/` kopieren
- Skin Shortcuts: Die Dateien in `addon_data/script.skinshortcuts/` mit dem Präfix `skin.arctic.zephyr.martian.signde` auf `skin.arctic.zephyr.modern` umbenennen (Kopie behalten). Vor dem Umbenennen auf der Box prüfen, welche Dateien vorhanden sind.


## In Arbeit: Einstellungs-Varianten A/B/C (pausiert zugunsten des OSD)
Mockups: A = Schwebend (Bald-nah), B = Seitenblatt (Google TV), C = Karten. Plan: alle drei in den Skin bauen, umschaltbar über `Skin.String(SettingsStyle)` (leer = A, `B`, `C`, `original`).
Schon im Skin (Commit 5181844):
- Texturen `common/modern-round14.png`, `modern-round20.png`, `modern-pill.png`, `modern-shade.png` sowie `buttons/modern-switch-{on,off}[-focus].png`
- Fonts in allen Fontsets: ModernTitle 64, ModernH2 40, ModernItem 30, ModernRow 28, ModernRowBold 28, ModernSmall 23, ModernCaption 22, ModernTile 26, ModernCard 32
- Strings 32100–32124 (en_gb/de_de); die Property `Short` an SettingsInfoItems (Kurzbeschreibung)
- Umschalter in den Skin-Einstellungen (Button 9790 vor „Hauptmenü-Stil“) mit der Variable `Label_SettingsStyle`
Offen: `Includes_SettingsModern.xml` mit den Hub- und Kategorie-Layouts, bedingte Includes in Settings.xml und SettingsCategory.xml.

## OSD (30.09.2026): Vorschläge
- Die Testumgebung spielt Videos ab: `kodi-start` setzt `KODI_AE_SINK=NULL`. Testfilm `Kaltfront.mkv` (3 min, 3 Kapitel, 2 Tonspuren, SRT) liegt in der Testbibliothek.
- TinyPPI (Codec-Info) läuft nur auf echtem CoreELEC und ist hier nicht testbar.
- Mockups: „Kino“ (Verlauf statt Balken, Titel und Chips oben links, Uhr und Endzeit oben rechts, dünne Leiste mit Kapitelmarken, runde Transport-Buttons mittig, Pillen für Audio/Untertitel) und „Kompakt“ (schwebendes, abgerundetes Panel mit Poster). Dazu Spulen mit Zeit-Bubble und OSD-Dialoge als dunkles Seitenblatt rechts.


## v0.2.0 (30.09.2026): OSD Kino/Kompakt
- Neue Datei `1080i/Includes_OSDModern.xml`, generiert von `tools/gen_osd_modern.py`. Nicht von Hand ändern!
- Umschalter: Skin-Einstellungen > Hauptmenü > „OSD-Design“ (Button 9791). `Skin.String(OSDStyle)`: leer = Kino, `kompakt`, `original`. Live-TV nutzt immer das Original.
- Kodi speichert Skin-Strings kleingeschrieben (`osdstyle`) in `addon_data/<skin>/settings.xml`.
- VideoOSD.xml und DialogSeekBar.xml nutzen bedingte Includes, die Original-Includes (OSD1-3/Seekbar1-3) greifen nur bei `original`.
- Kino: Pillen Audio/Untertitel links, runde Buttons (Zurück, Rückspulen, Play/Pause, Vorspulen, Weiter, Stop), Pillen Kapitel/Video/PPI/Info rechts. Kompakt: Panel mit Poster und 9 runden Icon-Buttons.
- PPI: `RunScript(script.signde.tinyppi,dialog)`. TinyPPI entscheidet selbst zwischen signde-PPI und P3i-PPI. Ohne TinyPPI wird `ActivateWindow(playerprocessinfo)` aufgerufen.
- Spulen ohne OSD: schlanke Leiste mit Zeit-Blase (100 gestaffelte Slide-Animationen auf Player.Progress).
- Bekannt: Der Regler-Knopf (progress righttexture) wanderte nicht mit und ist deshalb deaktiviert (`knob=False`).
- Testumgebung: `advancedsettings.xml` mit `algorithmdirtyregions=0`, sonst entstehen Artefakte (dunkles Rechteck).
- Test-ZIP ohne CJK-Fonts (39 MB), ohne Fontset „Default (Unicode)“ und ohne Store-Screenshots, damit sie unter 30 MB bleibt. Im Repo ist beides noch enthalten.

## v0.2.1 + GitHub-Repository (30.09.2026)
- Die CJK-Fonts (RobotoNotoCJKsc, 39 MB), das Fontset „Default (Unicode)“ und die Store-Screenshots sind jetzt **dauerhaft** entfernt. Die Skin-ZIP hat damit etwa 30 MB.
- **GitHub: `Sunset-1982/kodi-repo`** (öffentlich). Der Nutzer lädt per GitHub Desktop hoch. Aufbau:
  - `skin.arctic.zephyr.modern/`: Quellcode (Stand Commit 78bb846 aus der Sandbox)
  - `repository.sunset1982/`: Repo-Addon 1.0.0. Datadir: `https://raw.githubusercontent.com/Sunset-1982/kodi-repo/gh-pages/zips/`
  - `build_repo.py`: baut `_site/` (zips/addons.xml, .md5, `<id>/<id>-<ver>.zip`, index.html, Repo-ZIP im Wurzelverzeichnis)
  - `.github/workflows/build.yml`: bei jedem Push auf main wird gebaut und per peaceiris/actions-gh-pages auf `gh-pages` veröffentlicht
  - `tools/`: gen_osd_modern.py und das Test-Umgebungs-Skript; `docs/`: diese Doku
- Installationsquelle für Kodi: `https://sunset-1982.github.io/kodi-repo/` (GitHub Pages auf gh-pages stellen).
- **Künftig:** Die Quelle der Wahrheit ist das GitHub-Repo. Eine neue Session klont `Sunset-1982/kodi-repo` (in Claude Code in der Cloud mit verbundenem Repo kann Claude direkt pushen). Für ein Update die Version in addon.xml erhöhen und pushen.
- Offen: siehe unten.


## v0.3.0 (30.09.2026): Einstellungs-Designs A/B/C
- Generator `tools/gen_settings_modern.py` → `1080i/Includes_SettingsModern.xml` (Hub-Includes SettingsHub_A/B/C, Kategorie-Includes SettingsCat_A/B/C inkl. Templates 7–15 und 10/20, Item-Listen SettingsItemsModern/Top/Rest aus SettingsInfoItems).
- Original-Layouts ausgelagert in `1080i/Includes_SettingsOriginal.xml` (SettingsHub_Original, SettingsCat_Original).
- Settings.xml und SettingsCategory.xml wählen per `Skin.String(SettingsStyle)` (leer = A, `B`, `C`, `original`). Furniture_Header nur beim Original, bei B-Kategorie ohne Uhr und Wetter.
- Stolperfallen: Kodi-Labels kennen kein `aligny=bottom`. Einwortige Labels umbrechen nicht, deshalb laufen sie bei Fokus durch (`<scroll>`). Die „focusedlayout“-Kachel muss `Control.HasFocus(id)` prüfen, sonst ist bei zwei Listen in beiden eine weiß.
- Testumgebung: `tools/testenv/kodi-skinstring ID WERT` setzt Skin-Strings bei gestopptem Kodi.
- Nicht umgestaltet: Skin-Einstellungen, Systeminfo, Profile, Addon-Browser, Dateimanager (weiter Original-Optik).


## v0.4.0 (30.09.2026): OSD-Knopf, Dialoge als Seitenblatt, Live-TV
- **Regler-Knopf:** Ein Bild mit 100 gestaffelten Slide-Animationen auf Player.Progress, wie bei der Zeit-Blase. Der progress-righttexture-Trick funktioniert in Kodi nicht.
- **DialogSettings.xml:** `DialogSettings_Sheet` (Seitenblatt rechts, 860 px breit, Templates im Modern-Stil, Buttons 28/29/30 als Pillen) gilt, solange `OSDStyle` nicht `original` ist. Das Original liegt als `DialogSettings_Original` in Includes_SettingsOriginal.xml.
  - Stolperfalle: Eine Bedingung auf `Window.IsActive(fullscreenvideo)` im Include war unzuverlässig, weil Kodi den Dialog teils vorher lädt. Deshalb wurde sie entfernt.
  - Regler (sliderex): eigene schlanke Texturen `osd/modern/sliderbar.png` (64×16, 4 px Linie) und `slidernib.png` (16 px), sliderwidth 140.
- **Live-TV:** Das Modern-OSD gilt jetzt auch für Live-TV. Kino und Kompakt haben eigene TV-Gruppen (`kino_tv()`/`kompakt_tv()`) mit Senderlogo (Player.Art(thumb)), Sendung, Zeiten, „Als nächstes“ (VideoPlayer.NextTitle/NextStartTime) und PVR.EpgEventProgress (plus TimeshiftProgress). Kino hat die Pillen „Sender“ (pvrosdchannels) und „Programm“ (tvguide), die Video-Pille ist bei TV ausgeblendet. Kompakt hat alternative Buttons auf denselben Plätzen (507/511 und 509/512) mit bedingter Navigation.
- **Testumgebung Live-TV:** pvr.iptvsimple (in Flatpak-Kodi enthalten). `/home/claude/testmedia/tv/channels.m3u` (3 Sender auf Kaltfront.mkv), `epg.xml`, Logos. Konfiguriert über `addon_data/pvr.iptvsimple/instance-settings-1.xml` (m3uPath, epgPath). Nach dem Start etwa 15 s warten, bis die Sender geladen sind.

## Offen (Stand v0.4.0)
- Restliche Fenster im neuen Stil: Skin-Einstellungen, Systeminfo, Addon-Browser, Dateimanager, Profile, DialogSelect (Auswahllisten, z. B. Audiostream-Auswahl)
- Musik-OSD/Visualisierung


## v0.5.0 (30.09.2026): Farbsystem und Aufräumen
- **Farbvariablen** in Includes_Defs.xml: ModernBg, ModernSurface, ModernFocus, ModernFocusText, ModernAccent. Standard ist Graphit, der Wert kommt aus `Skin.String(<Name>)`. ColorFocusFrame nutzt ModernFocus.
- Beide Generatoren nutzen die Variablen statt fester Hex-Werte. Die Hintergrund-Abdunklung in den Einstellungen ist jetzt `common/modern-shade-w.png` (weiß mit Alpha-Verlauf) mit colordiffuse ModernBg. Sheets und Kompakt-Panel sind in ModernBg gefärbt.
- **Farbthemen** (Skript `tools/add_color_system.py`, idempotent): graphit, mitternacht, oled, nordlicht, sonnenuntergang, sand, kodiblau. Auswahl über Custom_1130 (DialogSelect) mit `includesetting=ModernTheme` und den Items `CustomSettings_Items.ModernTheme` (setzen alle 5 Strings plus ModernTheme). Label über `Label_ModernTheme`.
- **Skin-Einstellungen > Farben:** Abschnitt „Modern-Farben“ (97599 Überschrift, 9760 Farbthema, 9761–9765 Einzelfarben per `Skin.SetColor(Name,StringID,$VAR[Name],special://skin/extras/colors.xml)`, danach ModernTheme=custom; 9766 zurücksetzen). Stolperfalle: Die Überschrift bei Skin.SetColor muss eine reine String-ID sein, nicht `$LOCALIZE[...]`.
- **Ausgeblendet** (nur sichtbar bei OSDStyle=original): 9202, 9209, 9210, 9211, 92111, 9212, 9217, 9213, 92131, 9216, 9218, 9219, 9220, 9221, 9222. Farbverläufe 9653/9654 nur sichtbar, wenn OSD oder Einstellungen auf Original stehen. Nichts gelöscht, damit das Original-Design funktionsfähig bleibt.
- (Seit v0.6.0 gilt das Farbsystem überall, siehe unten.)


## v0.6.0 (30.09.2026): Farben einheitlich, Unschärfe im Hauptmenü
- Skript `tools/unify_colors.py` (idempotent, lässt die generierten Includes aus):
  - `ColorHighlight` und `ColorGradient` → ModernFocus, außer bei `ModernTheme=classic`.
  - Neue Variablen: `ColorHighlightText` (ModernFocusText / Selected), `ColorAccentText` (ModernAccent / ColorHighlight), `ColorListFocus` (ModernFocus / Dark1), `ColorListFocusText` und `ColorListFocusText2` (ModernFocusText / Light1 bzw. Light2).
  - In focusedlayouts mit Highlight werden helle text- und selectedcolor-Werte zu ColorHighlightText. `focusedcolor Selected` → ColorHighlightText. Radio-Fokus-Icons in FFFFFFFF → ColorHighlightText. `textcolor`/`[COLOR]` mit ColorHighlight → ColorAccentText.
  - Fokusbalken der Ansichten (box.png in Dark1, in focusedlayouts und *focus*-Includes) → ColorListFocus, Text darauf entsprechend.
- Thema **„Klassisch (Original-Farben)“** (ModernTheme=classic, String 32176). Die alten Optionen Akzentfarbe (9651) und Verlauf (9653/9654) sind nur bei Klassisch sichtbar.
- `colors/defaults.xml` übernimmt die Werte von „Dark with Dark Dialogs“ (8 Farben), Dialoge sind also standardmäßig dunkel. Helle Dialoge lassen sich weiter über Kodis Skin-Farben wählen, dort ist der Kontrast mit hellem Fokus aber schwächer.
- **Unschärfe:** existiert über TMDb Helper (Hintergrund > „Unschärfe aktivieren“, `TMDbHelper.EnableBlur`, Bild `Window(Home).Property(TMDbHelper.ListItem.BlurImage)`). Neu ist die Option 93121 „Unschärfe auch im Hauptmenü“ (`blur.home`), angepasst in Includes_Global.xml (GlobalBackground-Multiimages). In der Testumgebung startet der TMDb-Helper-Dienst nicht (keine ListItem-Properties), deshalb nur auf der Box testbar.
- Testumgebung: kodi-start setzt REQUESTS_CA_BUNDLE/SSL_CERT_FILE auf /etc/ssl/certs/ca-certificates.crt.


## v0.7.0 (30.09.2026): Kontext- und Powermenü als Karte (Variante A)
- Generator `tools/gen_menus_modern.py` erzeugt DialogContextMenu.xml, DialogButtonMenu.xml und Includes_MenusModern.xml (registriert in Includes.xml). Die Dateien nicht von Hand bearbeiten.
- **Kontextmenü (106):** Karte 560 px breit mit `common/modern-card.png` (Radius 24, weicher Schatten, 28 px Rand, border 52), gefärbt in ModernBg. Kopf: Art des Eintrags (`ModernContextCaption` nach ListItem.DBType) und Titel (`ModernContextTitle`). Die Buttons haben als Fokus eine abgerundete Fläche (modern-round14) in ModernFocus, Text in ModernFocusText, 14 px Abstand zum Kartenrand.
  - Stolperfalle: Kodi setzt die Höhe von Bild 999 auf `XML-Höhe − XML-Höhe der Grouplist (max 700) + tatsächliche Höhe der Grouplist`. Deshalb ist die XML-Höhe 118 + 700 + 14 + 56.
- **Powermenü (111):** gleiche Karte, Kopf mit Datum/Uhrzeit und „Power-Menü“. Liste 3110 aus skinshortcuts-group-powermenu. Kartenhöhe über 10 bedingte Hintergründe (NumItems). Symbole `osd/modern/pm-*.png` über `ModernPowerIcon` (Teilstring von ListItem.Property(path)). Timer-Regeln stehen vor powerdown/shutdown, weil der Timer-Pfad „shutdowntimer“ enthält.
- Alte Menüs mit unlesbarem Fokus (helles Grau, Text Black70 aus DefContextButton) sind damit ersetzt. Getestet mit Graphit und Sonnenuntergang.


## v0.8.0 (30.09.2026): Fehler von der Box
- **Zeitstrahl:** Kodi skaliert beim Fortschrittsbalken die midtexture über die Pixelhöhe der texturebg. Bei leerer `<texturebg />` ist der Faktor 1, der Füllbalken wird 8 statt 6 px hoch und rutscht um 4 px nach unten (Kodi rechnet den Versatz mit `fabs`). Lösung: Alle Fortschrittsbalken in gen_osd_modern.py haben jetzt `bar.png` mit `colordiffuse 00ffffff` als unsichtbaren Hintergrund.
- **DialogSettings** (Audio-, Untertitel- und Videoeinstellungen) nutzt immer `DialogSettings_Sheet`. Ursache für das Original-Layout auf der Box: Diese Dialoge sind KEEP_IN_MEMORY. Bedingte Includes werden dadurch nur beim ersten Laden ausgewertet, und nach einem Wechsel des OSD-Designs bleibt die alte Variante bis zum Skin-Neuladen aktiv.
- **Farbthema-Liste repariert:** Das Klassisch-Item (v0.6.0) stand innerhalb des Graphit-Items. Das `CustomSettings_Items.ModernTheme`-Include war dadurch vorzeitig geschlossen, und nur Graphit war auswählbar. Klassisch ist jetzt das letzte Item.
- **Dateimanager:** Panels als abgerundete Karte (modern-round20, ModernBg), Fokus als eingerückte abgerundete Fläche (ModernFocus), in der inaktiven Liste ModernSurface. Textfarben über `ModernFileText20/21` (in gen_menus_modern.py).
- **Einstellungen Design A:** Liste 5 ist 612 statt 660 hoch und endet damit über der Uhr.
- Offen: Auf den Fotos der Box war die Schrift auf dem Fokus hell. Im Emulator ist sie dunkel, vermutlich wurde auf der Box „Text auf Fokus“ geändert. Lösung: Farbthema neu wählen oder Modern-Farben zurücksetzen.


## v0.8.1 (30.09.2026): Neues Logo (Eisberg aus Vorschlag 5 in Schwarz/Weiß plus Typografie aus Vorschlag 8)
- `icon.png` (512 px): Eisberg-Symbol (weiß, graue Schattenflächen, graue Horizontlinie) über „arctic / zephyr / modern.“ in DM Sans (grau, weiß, hellgrau) auf #101317. Das Symbol lässt sich auch einzeln verwenden. Die Vorlage liegt in `tools/logo.html` (Playwright-Render, #skin #symbol #repo #word).
- `media/misc/logo-modern.png` (1510×154, Eisberg + Schriftzug, transparent, farbig) ersetzt `misc/martian.png`, das gelöscht ist. Dabei beachten: `media/Textures.xbt` enthält noch alte Martian-Grafiken. Neue Grafiken deshalb immer unter neuem Namen anlegen, weil Kodi sonst die gleichnamige Datei aus der XBT lädt.
- Startbildschirm (Custom_1198): Das Text-Label „Arctic Zephyr“ ist entfernt, das Logo steht zentriert (900×94, keep). In den Skin-Einstellungen („Über“) ist Label 9901 ausgeblendet, Bild 9902 zeigt das neue Logo.
- `fanart.jpg` zeigt jetzt einen Screenshot des neuen Hauptmenüs. Repository-Addon 1.0.1 mit eigenem Icon „sunset / 1982 / repo.“ und derselben Fanart. Kodi zeigt das neue Repo-Icon erst nach dem Update des Repo-Addons.
