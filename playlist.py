from datetime import datetime
from pathlib import Path  
import pandas as pd

from tracks import Track



class Playlist():

    def __init__(self, sp, name, uri) -> None:
        self.sp = sp
        self.name = name
        self.uri = uri
        self.tracks = self.extract()

    def extract_tracks(self):
        
    
    def extract(self):
        # retrieving tracks from spotify
        tracks = self.sp.playlist_items(self.uri)

        # cleaning track and feature analysis from API and places in a DataFrame
        tracks_playlist_df = self.get_playlist_data_df(tracks)    
        # features_playlist_df = self.get_track_feature_df(tracks_playlist_df)

        # # Merging track info and feature analysis on the id contained in the uri
        # playlist_df = pd.merge(tracks_playlist_df, features_playlist_df, on='id', how='outer')
        # playlist_df.set_index('id', inplace=True)
        pass
        # return playlist_df

    def get_playlist_data_df(self, tracks):
        data = {}

        for item in tracks['items']:
            track = item['track']

            id = track['id']
            popularity = track['popularity']
            uri = track['uri']
           
            track_obj = Track(self.sp, id, uri, self.uri, popularity)
            data[id] = track_obj
            
        print(data)
        

        return data
    
    def get_track_feature_df(self, tracks_playlist_df):

        track_ids = tracks_playlist_df['id'].to_list()
        track_features = self.sp.audio_features(track_ids)

        for features in track_features:
            # Filling in a Null return of audio analysis
            if features is None:
                features['acousticness'].append(None) 
                features['analysis_url'].append(None)
                features['danceability'].append(None)
                features['duration_ms'].append(None)
                features['energy'].append(None)
                features['instrumentalness'].append(None)
                features['key'].append(None)
                features['liveness'].append(None)
                features['loudness'].append(None)
                features['mode'].append(None)
                features['speechiness'].append(None)
                features['tempo'].append(None)
                features['time_signature'].append(None)
                features['track_href'].append(None)
                features['valence'].append(None)

        features_playlist_df = pd.DataFrame(track_features)
        return features_playlist_df
    
    # def save_to_csv(self):
    #     self.tracks.to_csv(self.filepath)