# Arctic: Zephyr - Modern

Ein moderner Kodi-Skin für CoreELEC 21 (Kodi 21 Omega), abgeleitet von **Arctic: Zephyr - Martian (avdvplus/p3i)** von signde.
Credits: jurialmunkey, beatmasterrs, martian89, jamal2362, signde. Anpassungen: Sunset1982.
Lizenz: Creative Commons BY-NC-SA 3.0 (siehe `skin.arctic.zephyr.modern/LICENSE.txt`).

## Inhalt dieses Repos

| Ordner/Datei | Zweck |
|---|---|
| `skin.arctic.zephyr.modern/` | Quellcode des Skins |
| `repository.sunset1982/` | Kodi-Repository-Addon (einmal installieren, danach kommen Updates automatisch) |
| `build_repo.py` | baut aus den Ordnern die Kodi-Repository-Dateien |
| `.github/workflows/build.yml` | GitHub Action: baut bei jedem Push automatisch und veröffentlicht auf dem Branch `gh-pages` |
| `tools/` | Generator für das OSD (`gen_osd_modern.py`) und Skripte für die Test-Umgebung |
| `docs/` | Änderungsprotokoll und Beschreibung der Test-Umgebung |

## Einmalige Einrichtung auf GitHub

1. Auf github.com ein **neues, öffentliches** Repository `kodi-repo` anlegen (ohne README).
2. In **GitHub Desktop**: *File → Clone repository* → `Sunset-1982/kodi-repo` klonen.
3. Den **Inhalt** dieses Pakets in den geklonten Ordner kopieren. Wichtig ist auch der versteckte Ordner `.github`.
4. In GitHub Desktop eine Beschreibung eintragen, dann auf **Commit to main** und anschließend auf **Push origin** klicken.
5. Auf github.com unter **Actions** prüfen, ob „Kodi-Repository bauen“ grün durchläuft (1–2 Minuten).
6. Unter **Settings → Pages** als Quelle *Deploy from a branch* und dann **gh-pages** / *(root)* wählen und speichern.
   Danach ist die Installationsseite unter `https://sunset-1982.github.io/kodi-repo/` erreichbar.

## Installation auf dem Player (einmalig)

1. Kodi → Einstellungen → System → Addons: **Unbekannte Quellen** aktivieren.
2. Einstellungen → Dateimanager → **Quelle hinzufügen** → `https://sunset-1982.github.io/kodi-repo/` → Name z. B. `sunset`.
3. Addons → **Aus ZIP-Datei installieren** → `sunset` → `repository.sunset1982-1.0.0.zip`.
4. Addons → **Aus Repository installieren** → *Sunset1982 Repository* → Aussehen → Skin → **Arctic: Zephyr - Modern**.

Ab jetzt holt sich Kodi neue Versionen automatisch, sobald im Skin die Versionsnummer in `addon.xml` erhöht und gepusht wurde.

## Voraussetzungen auf dem Player
Die Abhängigkeiten (Skin Variables, Skin Shortcuts, TMDb Helper, signde TinyPPI …) kommen aus dem **signde-Repository**. Wer den Martian-Skin schon nutzt, hat sie bereits.

## Einstellungen des alten Skins übernehmen (optional)
Auf der Box (per SMB/SSH) den Ordner
`/storage/.kodi/userdata/addon_data/skin.arctic.zephyr.martian.signde/`
nach
`/storage/.kodi/userdata/addon_data/skin.arctic.zephyr.modern/` kopieren. Die Menüs von Skin Shortcuts liegen in `addon_data/script.skinshortcuts/`. Dort die Dateien mit dem Präfix `skin.arctic.zephyr.martian.signde` als Kopie mit dem Präfix `skin.arctic.zephyr.modern` anlegen.

## Neue Version veröffentlichen
1. Änderungen im Ordner `skin.arctic.zephyr.modern/` vornehmen.
2. In `skin.arctic.zephyr.modern/addon.xml` die `version` erhöhen (z. B. 0.2.1 → 0.2.2).
3. Committen und pushen. Die Action baut alles neu, und Kodi zeigt das Update an.
