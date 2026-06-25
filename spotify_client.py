import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from auth.spotify_auth import SpotifyAuth


def get_spotify_client():
    # Load variables from .env
    load_dotenv()
    
    auth = SpotifyAuth()
    return auth.get_client()

    # Create and return Spotify client
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
            scope="""
            playlist-read-private
            playlist-read-collaborative
            playlist-modify-private
            playlist-modify-public
            """
        )
    )

    return sp