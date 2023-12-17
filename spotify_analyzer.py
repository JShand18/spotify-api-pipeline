import spotipy
import csv
import boto3
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd

from config.playlist_uri_lib import spotify_top_playlists, spotify_new_playlists
from playlist import Playlist

load_dotenv()


def extract_playlist():
    PLAYLIST = 'Top_50_USA'

    sp = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

    top_playlists = spotify_top_playlists()
    for uri in top_playlists:
        top_playlist = Playlist(sp, uri, top_playlists[uri])
        
        print(top_playlist.tracks)


if __name__ == '__main__':
    extract_playlist()

