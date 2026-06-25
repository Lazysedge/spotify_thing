def generate_playlist(
    songs,
    mood=None,
    genre=None,
    energy=None
):
    playlist = []

    for song in songs:

        if mood:
            if song.get("mood") != mood:
                continue

        if genre:
            if song.get("genre") != genre:
                continue

        if energy:
            if song.get("energy") != energy:
                continue

        playlist.append(song)

    return playlist