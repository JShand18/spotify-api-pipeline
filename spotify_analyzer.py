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
        top_playlist.save_to_csv()

    new_playlists = spotify_new_playlists()
    for uri in new_playlists:
        new_playlist = Playlist(sp, uri, new_playlists[uri])
        new_playlist.save_to_csv()


if __name__ == '__main__':
    extract_playlist()

