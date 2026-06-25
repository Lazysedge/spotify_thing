import customtkinter as ctk


class PlaylistPanel(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        spotify_client
    ):
        super().__init__(parent)

        self.sp = spotify_client

        self.playlist_ids = []

        self.playlist_box = ctk.CTkComboBox(
            self,
            values=[]
        )

        self.playlist_box.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.refresh_button = ctk.CTkButton(
            self,
            text="Refresh Playlists",
            command=self.load_playlists
        )

        self.refresh_button.pack(
            pady=10
        )

    def load_playlists(self):

        playlists = (
            self.sp.current_user_playlists()
        )

        names = []
        self.playlist_ids.clear()

        for playlist in playlists["items"]:

            names.append(
                playlist["name"]
            )

            self.playlist_ids.append(
                playlist["id"]
            )

        self.playlist_box.configure(
            values=names
        )

        if names:
            self.playlist_box.set(
                names[0]
            )

    def get_selected_playlist_id(self):

        selected = (
            self.playlist_box.get()
        )

        index = (
            self.playlist_box.cget(
                "values"
            ).index(selected)
        )

        return self.playlist_ids[index]