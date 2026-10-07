# Zephyr Modern: einfarbigen Hintergrund auswaehlen (setzt zm.bgcolor und schaltet auf "Einfarbig")
import xbmc, xbmcgui
COLORS = [("", 31167), ("graphit", 31161), ("nachtblau", 31162), ("ozeanblau", 31163),
          ("tiefschwarz", 31164), ("petrol", 31165), ("aubergine", 31166)]
current = xbmc.getInfoLabel("Skin.String(zm.bgcolor)")
items = []
for key, sid in COLORS:
    li = xbmcgui.ListItem(xbmc.getLocalizedString(sid))
    icon = "special://skin/media/common/swatch-%s.png" % (key or "theme")
    li.setArt({"icon": icon, "thumb": icon})
    items.append(li)
pre = next((k for k, (n, _) in enumerate(COLORS) if n == current), 0)
sel = xbmcgui.Dialog().select(xbmc.getLocalizedString(31160), items, preselect=pre, useDetails=True)
if sel >= 0:
    key = COLORS[sel][0]
    if key:
        xbmc.executebuiltin("Skin.SetString(zm.bgcolor,%s)" % key)
    else:
        xbmc.executebuiltin("Skin.Reset(zm.bgcolor)")
    xbmc.executebuiltin("Skin.SetString(zm.bgmode,color)")
