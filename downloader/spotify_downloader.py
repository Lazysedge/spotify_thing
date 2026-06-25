from downloader.worker import (
    download_with_spotdl
)


class SpotifyDownloader:

    def __init__(self):
        self.active_downloads = []

    def download_song(
        self,
        spotify_url,
        output_folder,
        audio_format="mp3"
    ):

        download_with_spotdl(
            spotify_url,
            output_folder,
            audio_format
        )

    def download_playlist(
        self,
        spotify_urls,
        output_folder,
        audio_format="mp3"
    ):

        for url in spotify_urls:

            self.download_song(
                url,
                output_folder,
                audio_format
            )