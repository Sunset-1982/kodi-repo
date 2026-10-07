# Zephyr Modern: spielt in der Flix-Ansicht nach kurzer Pause den Trailer des fokussierten Titels im Hintergrund ab.
# Läuft nur, solange das Video-Fenster offen und Skin.HasSetting(zm.autotrailer) aktiv ist.
import xbmc, xbmcgui

HOME = xbmcgui.Window(10000)
DELAY = 3.0   # Sekunden Stillstand, bevor der Trailer startet
STEP = 0.25


def cond(c):
    return xbmc.getCondVisibility(c)


def info(i):
    return xbmc.getInfoLabel(i)


def main():
    if HOME.getProperty('zm.trailer.running'):
        return
    HOME.setProperty('zm.trailer.running', '1')
    mon, player = xbmc.Monitor(), xbmc.Player()
    last, still, playing = None, 0.0, ''
    try:
        while not mon.abortRequested() and cond('Window.IsActive(videos)') and cond('Skin.HasSetting(zm.autotrailer)'):
            key = info('Container.FolderPath') + '|' + info('ListItem.Label') if cond('Control.HasFocus(52)') else None
            if key != last:
                last, still = key, 0.0
                if playing:
                    stop(player, playing)
                    playing = ''
            else:
                still += STEP
            trailer = info('ListItem.Trailer') if key else ''
            if trailer and not playing and still >= DELAY and not cond('Player.HasMedia'):
                player.play(trailer, windowed=True)
                playing = trailer
                HOME.setProperty('zm.trailer', '1')
            if playing and not cond('Player.HasMedia') and still > DELAY + 5:
                playing = ''  # Trailer zu Ende
                HOME.clearProperty('zm.trailer')
            if mon.waitForAbort(STEP):
                break
    finally:
        if playing:
            stop(player, playing)
        HOME.clearProperty('zm.trailer')
        HOME.clearProperty('zm.trailer.running')


def stop(player, playing):
    # Nur den eigenen Trailer stoppen, nie eine vom Nutzer gestartete Wiedergabe
    if HOME.getProperty('zm.trailer') and cond('Player.HasMedia') and not cond('Player.IsFullscreen'):
        try:
            if player.getPlayingFile() == playing or 'plugin://' in playing:
                player.stop()
        except RuntimeError:
            pass
    HOME.clearProperty('zm.trailer')


main()
