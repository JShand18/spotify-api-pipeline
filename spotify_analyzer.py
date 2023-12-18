import spotipy
import boto3
import os
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd

from config.playlist_uri_lib import spotify_top_playlists, spotify_new_playlists
from playlist import Playlist

load_dotenv()

def extract_playlist(name, uri, sp, s3):
    # Creating a new playlist object to handle feature extraction and file handling
    playlist = Playlist(sp, name, uri)
    playlist.save_to_csv

    # Sending playlist csv to s3 bucket
    date = datetime.now()
    filename = f'{date.year}/{date.month}/{date.day}/{playlist.filename}'
    response = s3.Object('spotify-analysis-data', filename).upload_file(playlist.filepath)


def extract_all():
    # Spotify client connect using credientials stored in .env
    sp = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())
    access_key = os.getenv('ACCESS_KEY')
    secret_key = os.getenv('SECRET_KEY')
    s3 = boto3.resource('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    for bucket in s3.buckets.all():
        print(bucket.name)

    # Retrieving playlist names and uri
    top_playlists = spotify_top_playlists()
    for playlist in top_playlists:
        extract_playlist(playlist, top_playlists[playlist], sp, s3)

    new_playlists = spotify_new_playlists()
    for playlist in new_playlists:
        extract_playlist(playlist, new_playlists[playlist], sp, s3)


def lambda_handler(event, context):
    extract_all()


if __name__ == '__main__':
    extract_all()

