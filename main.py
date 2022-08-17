import os
import spotipy
import subprocess
from os import popen
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_CLIENT_ID=os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET=os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID, 
    client_secret=SPOTIFY_CLIENT_SECRET
))

def playlists(user):
    if user:
        return sp.user_playlists(user)
    else:
        return "null"
        
playlists.__doc__ = "Return all public playlists from a specified user"

list = []

for item in playlists("stayglued")["items"]:
    list.append(item['name'])


# TEST=popen(f"gum input --placeholder 'test'")
# print(TEST)
