import argparse
import os
import spotipy
import subprocess
from spotipy.oauth2 import SpotifyClientCredentials
from iterfzf import iterfzf

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"), 
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

username = input("Enter spotify username: ")
list = []

def playlists(user):
    if user:
        offset = 0
        return sp.user_playlists(user,limit=50,offset=offset)
    else:
        return "null"
        
playlists.__doc__ = "Return all public playlists from a specified user"

if username:
    for item in playlists(username)["items"]:
        list.append(item['name'])
    iterfzf(list)
else:
    print("Not a valid username")
