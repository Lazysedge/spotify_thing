import pandas as pd


def export_playlist_to_csv(tracks, filename="playlist_export.csv"):

    songs = []

    for item in tracks:

        track = item.get("track")

        if track is None:
            track = item.get("item")

        if track is None:
            continue

        song_data = {
            "Song Name": track.get("name"),
            "Artist": ", ".join(
                artist["name"]
                for artist in track.get("artists", [])
            ),
            "Album": track.get(
                "album",
                {}
            ).get(
                "name",
                "Unknown Album"
            ),
            "Duration (seconds)": round(
                track.get(
                    "duration_ms",
                    0
                ) / 1000
            ),
            "Spotify ID": track.get("id"),
            "Spotify URI": track.get("uri"),
            "Popularity": track.get("popularity"),
            "Explicit": track.get("explicit")
        }

        songs.append(song_data)

    df = pd.DataFrame(songs)

    df.to_csv(
        filename,
        index=False,
        encoding="utf-8-sig"
    )

    print(
        f"\nPlaylist exported successfully to:\n{filename}"
    )