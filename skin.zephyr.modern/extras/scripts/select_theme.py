# Zephyr Modern: Farbthema auswaehlen (setzt Kodis Farbschema, eigene Farben werden zurueckgesetzt)
import json, xbmc, xbmcgui
THEMES = [("SKINDEFAULT", 31101), ("Mitternacht", 31102), ("OLED Schwarz", 31103), ("Nordlicht", 31104),
          ("Sonnenuntergang", 31105), ("Sand", 31106), ("Kodi-Blau", 31107)]
VARS = ["ModernBg", "ModernSurface", "ModernFocus", "ModernFocusText", "ModernAccent", "ModernBorder"]
current = xbmc.getInfoLabel("Skin.CurrentColourTheme") or "SKINDEFAULT"
labels = [xbmc.getLocalizedString(i) or n for n, i in THEMES]
pre = next((k for k, (n, _) in enumerate(THEMES) if n == current), 0)
sel = xbmcgui.Dialog().select(xbmc.getLocalizedString(31100), labels, preselect=pre)
if sel >= 0:
    for v in VARS:
        xbmc.executebuiltin("Skin.Reset(%s)" % v)
    xbmc.executeJSONRPC(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "Settings.SetSettingValue",
                                    "params": {"setting": "lookandfeel.skincolors", "value": THEMES[sel][0]}}))
