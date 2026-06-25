import customtkinter as ctk
from tkinter import filedialog


class DownloadPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.download_folder = ""

        # -------------------------
        # Title
        # -------------------------
        self.title_label = ctk.CTkLabel(
            self,
            text="Downloads",
            font=("Arial", 20, "bold")
        )

        self.title_label.pack(
            pady=(10, 15)
        )

        # -------------------------
        # Song URL input
        # -------------------------
        self.song_label = ctk.CTkLabel(
            self,
            text="Spotify Song URL"
        )

        self.song_label.pack()

        self.song_entry = ctk.CTkEntry(
            self,
            width=500,
            placeholder_text="https://open.spotify.com/track/..."
        )

        self.song_entry.pack(
            pady=5
        )

        self.download_song_button = ctk.CTkButton(
            self,
            text="Download Song",
            command=self.download_song
        )

        self.download_song_button.pack(
            pady=10
        )

        # -------------------------
        # Playlist URL input
        # -------------------------
        self.playlist_label = ctk.CTkLabel(
            self,
            text="Spotify Playlist URL"
        )

        self.playlist_label.pack(
            pady=(20, 0)
        )

        self.playlist_entry = ctk.CTkEntry(
            self,
            width=500,
            placeholder_text="https://open.spotify.com/playlist/..."
        )

        self.playlist_entry.pack(
            pady=5
        )

        self.download_playlist_button = ctk.CTkButton(
            self,
            text="Download Playlist",
            command=self.download_playlist
        )

        self.download_playlist_button.pack(
            pady=10
        )

        # -------------------------
        # CSV Import
        # -------------------------
        self.csv_button = ctk.CTkButton(
            self,
            text="Import CSV Playlist",
            command=self.import_csv
        )

        self.csv_button.pack(
            pady=20
        )

        # -------------------------
        # Download Folder
        # -------------------------
        self.folder_button = ctk.CTkButton(
            self,
            text="Select Download Folder",
            command=self.select_folder
        )

        self.folder_button.pack(
            pady=10
        )

        self.folder_label = ctk.CTkLabel(
            self,
            text="No folder selected"
        )

        self.folder_label.pack()

    # ==================================
    # Folder Selection
    # ==================================
    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:
            self.download_folder = folder

            self.folder_label.configure(
                text=folder
            )

    # ==================================
    # Song Download
    # ==================================
    def download_song(self):

        url = self.song_entry.get()

        if not url:
            print(
                "No song URL provided."
            )
            return

        print(
            f"Downloading song:\n{url}"
        )

        # Future:
        # downloader.download_song(url)

    # ==================================
    # Playlist Download
    # ==================================
    def download_playlist(self):

        url = self.playlist_entry.get()

        if not url:
            print(
                "No playlist URL provided."
            )
            return

        print(
            f"Downloading playlist:\n{url}"
        )

        # Future:
        # downloader.download_playlist(url)

    # ==================================
    # CSV Import
    # ==================================
    def import_csv(self):

        file_path = filedialog.askopenfilename(
            filetypes=[
                (
                    "CSV Files",
                    "*.csv"
                )
            ]
        )

        if not file_path:
            return

        print(
            f"CSV imported:\n{file_path}"
        )