import os


CACHE_PATH = ".spotify_cache"


def get_cache_path():
    return CACHE_PATH


def clear_cache():
    if os.path.exists(CACHE_PATH):
        os.remove(CACHE_PATH)
        print("Spotify cache removed.")