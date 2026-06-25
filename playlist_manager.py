# ----------------------------------------
# Show current user information
# ----------------------------------------
def show_user_info(sp):
    user = sp.current_user()

    print("\n===================================")
    print("Logged in as:", user.get("display_name"))
    print("Spotify ID :", user.get("id"))
    print("===================================\n")


def get_playlist_name(sp, playlist_id):
    playlist = sp.playlist(playlist_id)
    return playlist["name"]
# ----------------------------------------
# Show playlists and let user choose one
# ----------------------------------------
def choose_playlist(sp):
    playlists_response = sp.current_user_playlists()

    playlist_ids = []


    print("Your playlists:\n")

    for index, playlist in enumerate(
        playlists_response["items"],
        start=1
    ):
        print(
            f"{index}. {playlist['name']}"
        )

        playlist_ids.append(
            playlist["id"]
        )

    choice = int(
        input(
            "\nChoose playlist number: "
        )
    )

    playlist_id = playlist_ids[
        choice - 1
    ]

    return playlist_id


# ----------------------------------------
# Download ALL tracks
# Supports playlists with >50 songs
# ----------------------------------------
def get_all_tracks(
    sp,
    playlist_id
):
    results = sp.playlist_tracks(
        playlist_id
    )

    all_tracks = results["items"]

    while results["next"]:
        results = sp.next(results)
        all_tracks.extend(
            results["items"]
        )

    return all_tracks


# ----------------------------------------
# Print tracks nicely
# ----------------------------------------
def print_tracks(
    tracks
):
    print("\nTracks:\n")

    song_number = 1

    for item in tracks:

        track = item.get("track")

        if track is None:
            track = item.get("item")

        if track is None:
            continue

        song_name = track.get(
            "name",
            "Unknown Song"
        )

        artists = track.get(
            "artists",
            []
        )

        artist_name = (
            artists[0]["name"]
            if artists
            else "Unknown Artist"
        )

        album_name = (
            track.get(
                "album",
                {}
            )
            .get(
                "name",
                "Unknown Album"
            )
        )

        duration_seconds = (
            track.get(
                "duration_ms",
                0
            ) / 1000
        )

        print(
            f"{song_number}. "
            f"{song_name}"
        )

        print(
            f"   Artist : "
            f"{artist_name}"
        )

        print(
            f"   Album  : "
            f"{album_name}"
        )

        print(
            f"   Length : "
            f"{duration_seconds:.0f} seconds"
        )

        print()

        song_number += 1
    
