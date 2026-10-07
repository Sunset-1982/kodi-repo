# Arctic Zephyr - Modern: setzt das Kodi-Farbschema (Einstellungen > Oberflaeche > Skin > Farben)
import sys, json, xbmc
value = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else "SKINDEFAULT"
xbmc.executeJSONRPC(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "Settings.SetSettingValue",
                                "params": {"setting": "lookandfeel.skincolors", "value": value}}))
