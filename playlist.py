import spotipy
import csv
import boto3
from datetime import datetime
import pandas as pd


class Playlist():

    def __init__(self, sp, name, uri) -> None:
        self.sp = sp
        self.name = name
        self.uri = uri
        self.tracks = self.extract()

    
    def extract(self):
        tracks = self.sp.playlist_items(self.uri)
        tracks_playlist_df = self.get_playlist_data_df(tracks)    
        features_playlist_df = self.get_track_feature_df(tracks_playlist_df)
        playlist_df = pd.merge(tracks_playlist_df, features_playlist_df, on='id', how='outer')
        playlist_df.set_index('id', inplace=True)
        return playlist_df

    def get_playlist_data_df(self, tracks):
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
    
    def get_track_feature_df(self, tracks_playlist_df):
        track_ids = tracks_playlist_df['id'].to_list()

        track_features = self.sp.audio_features(track_ids)
        features_playlist_df = pd.DataFrame(track_features)
        return features_playlist_df
    