from rapidfuzz import fuzz


def find_exact_duplicates(tracks):
    """
    Detect duplicates using Spotify Track ID.
    """

    seen_tracks = set()
    duplicates = []

    for position, item in enumerate(tracks):

        track = item.get("track")

        if track is None:
            track = item.get("item")

        if track is None:
            continue

        track_id = track.get("id")

        if track_id is None:
            continue

        if track_id in seen_tracks:
            duplicates.append({
                "uri": track["uri"],
                "positions": [position]
            })
        else:
            seen_tracks.add(track_id)

    return duplicates


def find_fuzzy_duplicates(
    tracks,
    similarity_threshold=90,
    max_duration_difference=10000
):
    """
    Detect duplicates using:
    - song title similarity
    - artist similarity
    - duration similarity
    """

    seen_songs = []
    duplicates = []

    for position, item in enumerate(tracks):

        track = item.get("track")

        if track is None:
            track = item.get("item")

        if track is None:
            continue

        song_name = track.get(
            "name",
            ""
        ).lower().strip()

        artist_name = (
            track.get(
                "artists",
                [{}]
            )[0]
            .get(
                "name",
                ""
            )
            .lower()
            .strip()
        )

        current_key = (
            f"{song_name} {artist_name}"
        )

        duplicate_found = False

        for existing in seen_songs:

            similarity = fuzz.ratio(
                current_key,
                existing["key"]
            )

            duration_difference = abs(
                track.get(
                    "duration_ms",
                    0
                )
                - existing["duration"]
            )

            if (
                similarity >= similarity_threshold
                and duration_difference <= max_duration_difference
            ):

                duplicate_found = True

                duplicates.append({
                    "uri": track["uri"],
                    "positions": [position]
                })

                print("\nDuplicate detected")
                print(
                    f"Keep   : "
                    f"{existing['name']}"
                )
                print(
                    f"Remove : "
                    f"{track['name']}"
                )
                print(
                    f"Similarity: "
                    f"{similarity:.1f}%"
                )
                print(
                    f"Duration difference: "
                    f"{duration_difference/1000:.1f}s"
                )

                break

        if not duplicate_found:

            seen_songs.append({
                "key": current_key,
                "name": track["name"],
                "duration": track.get(
                    "duration_ms",
                    0
                )
            })

    return duplicates


def remove_duplicates(
    sp,
    playlist_id,
    duplicates
):
    """
    Remove duplicates from playlist.
    """

    if len(duplicates) == 0:
        print(
            "\nNo duplicates to remove."
        )
        return

    sp.playlist_remove_specific_occurrences_of_items(
        playlist_id,
        duplicates
    )

    print(
        f"\nRemoved "
        f"{len(duplicates)} "
        f"duplicate songs."
    )