SPOTIFY_SCOPES = [
    "playlist-read-private",
    "playlist-read-collaborative",
    "playlist-modify-private",
    "playlist-modify-public"
]


def get_scope_string():
    return " ".join(SPOTIFY_SCOPES)