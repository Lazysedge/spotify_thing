class SpotifyAIGui(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.sp = get_spotify_client()

        build_main_window(self)

        user = self.sp.current_user()

        self.account_panel.update_user(
            user
        )

        self.playlist_panel.load_playlists()