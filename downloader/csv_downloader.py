import pandas as pd

from downloader.spotify_downloader import (
    SpotifyDownloader
)


def download_csv_playlist(
    csv_file,
    output_folder
):

    df = pd.read_csv(csv_file)

    downloader = SpotifyDownloader()

    for _, row in df.iterrows():

        uri = row.get(
            "Spotify URI"
        )

        if not uri:
            continue

        spotify_url = (
            uri
            .replace(
                "spotify:track:",
                "https://open.spotify.com/track/"
            )
        )

        downloader.download_song(
            spotify_url,
            output_folder
        )