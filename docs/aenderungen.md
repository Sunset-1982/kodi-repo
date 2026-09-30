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
- Offen: Einstellungs-Varianten A/B/C (Layouts), Regler-Knopf im OSD, Live-TV-OSD, OSD-Dialoge (Audio/Untertitel) als Seitenblatt.
