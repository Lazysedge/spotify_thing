import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from auth.scopes import get_scope_string
from auth.token_manager import get_cache_path


class SpotifyAuth:

    def __init__(self):
        load_dotenv()

        self.auth_manager = SpotifyOAuth(
            client_id=os.getenv(
                "SPOTIFY_CLIENT_ID"
            ),
            client_secret=os.getenv(
                "SPOTIFY_CLIENT_SECRET"
            ),
            redirect_uri=os.getenv(
                "SPOTIFY_REDIRECT_URI"
            ),
            scope=get_scope_string(),
            cache_path=get_cache_path()
        )

        self.sp = spotipy.Spotify(
            auth_manager=self.auth_manager
        )

    def get_client(self):
        return self.sp

    def get_current_user(self):
        return self.sp.current_user()

    def is_logged_in(self):
        try:
            self.sp.current_user()
            return True
        except Exception:
            return False

    def logout(self):
        from auth.token_manager import clear_cache
        clear_cache()