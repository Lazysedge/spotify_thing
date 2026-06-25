from gui.account_panel import (
    AccountPanel
)

from gui.playlist_panel import (
    PlaylistPanel
)
from gui.progress_panel import ProgressPanel

from gui.settings_panel import SettingsPanel

from gui.download_panel import DownloadPanel
def build_main_window(app):

    app.account_panel = (
        AccountPanel(app)
    )

    app.account_panel.pack(
        fill="x",
        padx=20,
        pady=20
    )

    app.playlist_panel = (
        PlaylistPanel(
            app,
            app.sp
        )
    )

    app.playlist_panel.pack(
        fill="x",
        padx=20,
        pady=20
    )
    
    app.progress_panel = ProgressPanel(
    app
    )

    app.progress_panel.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )
    
    app.download_panel = DownloadPanel(
    app
    )

    app.download_panel.pack(
        fill="x",
        padx=20,
        pady=20
    )