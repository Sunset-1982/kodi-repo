# Test-Umgebung: Kodi-Emulation für Skin-Entwicklung

Zielgerät: Ugoos AM6B+ mit CoreELEC 21.3 (P3i T4c) → **Kodi 21.3 Omega**, xbmc.gui 5.17.0

## Grundlage des Projekts
**Arctic: Zephyr - Modern** (`skin.arctic.zephyr.modern`), abgeleitet von **Arctic: Zephyr - Martian (avdvplus/p3i)** (`skin.arctic.zephyr.martian.signde` 11.3.20.2, signde). Das Original hat der Nutzer als ZIP geliefert: `skin.arctic.zephyr.martian-58e645a…zip`. Die Änderungen stehen in `claude/aenderungen.md` und im Patch `claude/patches/modern-01.patch`.
Referenz/Inspiration: `skin.bald` 0.8.2 (dangerouslaser). Bald braucht Kodi 22 (xbmc.gui 5.18.0) und läuft deshalb nicht direkt auf 21.3. Die DM-Sans-Fonts stammen aus Bald.

## Setup in der Cloud-Sandbox (Ubuntu 24.04), bei neuer Session neu aufbauen
1. `apt-get update && apt-get install -y flatpak imagemagick x11-apps sqlite3`
2. `flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo`
3. `flatpak install -y --noninteractive flathub tv.kodi.Kodi` (war am 30.09.2026: 21.3-Omega)
4. D-Bus: `mkdir -p /run/dbus; rm -f /run/dbus/pid; dbus-daemon --system --fork`
5. Virtueller Bildschirm: `Xvfb :99 -screen 0 1920x1080x24 &`
6. Start: `DISPLAY=:99 flatpak run --nosocket=wayland --filesystem=/home/claude tv.kodi.Kodi --windowing=x11`
7. Einmal starten und wieder beenden, dann in `~/.var/app/tv.kodi.Kodi/data/userdata/guisettings.xml`: `services.webserver=true`, `services.webserverauthentication=false` (JSON-RPC auf Port 8080)
8. Deutsch: ZIP von https://mirrors.kodi.tv/addons/omega/resource.language.de_de/ nach `~/.var/app/tv.kodi.Kodi/data/addons/` entpacken, dann per JSON-RPC `Settings.SetSettingValue locale.language=resource.language.de_de`

Stolperfallen:
- Ein `pgrep -f kodi.bin` findet das eigene Skript. Stattdessen `pgrep -x kodi.bin` verwenden.
- Einige Kodi-Spiegelserver blockiert der Proxy. Downloads deshalb mit curl-Retry mehrfach versuchen.
- Die Zip-Downloads von GitHub sind gesperrt, `git clone` funktioniert dagegen.
- Ein neu hinzugekommenes Addon ist beim ersten Start deaktiviert. Also `Addons.SetAddonEnabled` ausführen und Kodi neu starten.
- JSON-RPC hat kein ExecuteBuiltin. Skin-Bools deshalb bei gestopptem Kodi direkt in `addon_data/<skin>/settings.xml` setzen.

## Abhängigkeiten
- Aus dem signde-Repo (https://signde.github.io/repository.signde/addons/zips/ID/ID-VERSION.zip), identisch mit der Box:
  - script.skinvariables 2.2.4
  - script.module.jurialmunkey 0.2.35
  - script.module.infotagger 0.0.9
  - plugin.video.themoviedb.helper 6.17.3
  - script.signde.tinyppi 17.2.7.5
- Aus dem Omega-Repo (`kodi-getaddon`): script.skinshortcuts, script.image.resource.select, resource.images.weathericons.white, script.module.qrcode, requests-Kette, bs4, addon.signals, unidecode, simpleeval
- `script.module.pil` gibt es im Omega-Repo nicht. Die Flatpak-Version bringt PIL aber mit, deshalb reicht ein Stub-Addon mit leerem `lib`.
- Den Skin per Symlink einbinden: `addons/skin.arctic.zephyr.modern` → `/home/claude/skins/azm` (Git-Repo mit allen Änderungen)
- Den Skin direkt in `guisettings.xml` setzen (`lookandfeel.skin`) und Kodi neu starten. Das vermeidet den „Skin behalten?“-Dialog.
- Test-Layout wie beim Nutzer: `home.vertical=true`, `homemenu.netflix=true` (Menü links, Widgets daneben)

## Testbibliothek
16 fiktive Filme unter `/home/claude/testmedia/Filme/<Titel (Jahr)>/`: Dummy-`.mkv`, NFO mit 4K/DV/TrueHD-Streamdetails, per ImageMagick erzeugte Verlaufs-Poster und -Fanarts. Die Quelle steht in `sources.xml`. Die Pfad-Zeile in `MyVideos131.db` (`path`-Tabelle: strContent=movies, strScraper=metadata.local) wird per sqlite3 bei gestopptem Kodi eingetragen, danach folgt `VideoLibrary.Scan`.

## Hilfsskripte (/home/claude/kodi/bin)
- `kodi-start` / `kodi-stop`
- `kodi-rpc METHODE '{params}'`, z. B. `kodi-rpc GUI.ActivateWindow '{"window":"videos"}'`
- `kodi-shot NAME [wartezeit]` → Screenshot des Bildschirms (1920×1080)
- `kodi-getaddon ID…` → installiert Addons samt Abhängigkeiten aus dem Omega-Repo
- Log: `~/.var/app/tv.kodi.Kodi/data/temp/kodi.log`

## Grenzen
Die Performance auf dem AM6B+ lässt sich hier nicht messen, und CoreELEC-eigene Menüs fehlen. Den finalen Test deshalb immer auf der Box machen. Menü-Anpassungen aus Skin Shortcuts liegen in den userdata der Box und nicht im Skin.
