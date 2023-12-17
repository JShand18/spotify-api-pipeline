import spotipy
import csv
import boto3
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd

from config.playlist_uri_lib import spotify_top_playlists, spotify_new_playlists
from playlist import Playlist

# load_dotenv()

def extract_playlist(name, uri, sp, s3_resource):
    # Creating a new playlist object to handle feature extraction and file handling
    playlist = Playlist(sp, name, uri)
    playlist.save_to_csv

    # Sending playlist csv to s3 bucket
    date = datetime.now()
    filename = f'{date.year}/{date.month}/{date.day}/{playlist.filename}'
    response = s3_resource.Object('spotify-analysis-data', filename).upload_file(playlist.filepath)

    return response

def extract_all():
    # Spotify client connect using credientials stored in .env
    sp = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())
    s3_resource = boto3.resource('s3')

    # Retrieving playlist names and uri
    top_playlists = spotify_top_playlists()
    for playlist in top_playlists:
        extract_playlist(playlist, top_playlists[playlist], sp, s3_resource)

    new_playlists = spotify_new_playlists()
    for playlist in new_playlists:
        extract_playlist(playlist, new_playlists[playlist], sp, s3_resource)


def lambda_handler(event, context):
    extract_all()


if __name__ == '__main__':
    extract_all()

