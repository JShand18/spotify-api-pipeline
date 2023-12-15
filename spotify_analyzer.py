import spotipy
import csv
import boto3
from datetime import datetime
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

from config.playlists import spotify_top_playlists, spotify_new_playlists

load_dotenv()


def extract_playlist():
    PLAYLIST = 'Top_50_USA'

    sp = spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials())

    playlists = spotify_top_playlists()
    for playlist in playlists:
        tracks = sp.playlist_items(playlists[playlist])
        tracks_playlist_df = get_playlist_data_df(tracks)    
        features_playlist_df = get_track_feature_df(tracks_playlist_df, sp)
        playlist_df = pd.merge(tracks_playlist_df, features_playlist_df, on='id', how='outer')
        print(playlist_df.to_string())                  

def get_playlist_data_df(tracks):

    data = {
        'id':[],
        'title':[],
        'artist':[],
        'popularity':[],
    }

    for item in tracks['items']:
        track = item['track']
        if track['id'] not in  data['id']:
            data['id'].append(track['id'])
            data['title'].append(track['name'])
            data['artist'].append(track['artists'][0]['name'])
            data['popularity'].append(track['popularity'])

    tracks_playlist_df = pd.DataFrame(data)
    return tracks_playlist_df


def get_track_feature_df(tracks_playlist_df, sp):
    track_ids = tracks_playlist_df['id'].to_list()

    track_features = sp.audio_features(track_ids)
    features_playlist_df = pd.DataFrame(track_features)
    return features_playlist_df




if __name__ == '__main__':
    extract_playlist()

