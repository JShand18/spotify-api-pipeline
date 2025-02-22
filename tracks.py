from datetime import datetime
from pathlib import Path  
import pandas as pd

class Track():

    def __init__(self, sp, parent_uri, uri) -> None:
        self.sp = sp
        self.uri = uri
        self.parent_uri = parent_uri
        self.details = self.get_details()
        self.id = self.get_id()
        self.popularity = self.get_popularity()
        self.features = self.get_features()
        self.analysis = self.get_analysis()
        

    def get_details(self):
        return self.sp.track(self.uri)
    
    def get_id(self):
        return self.details['id']
    
    def get_popularity(self):
        return self.details['popularity']

    def get_features(self):
        return self.sp.audio_features(self.uri)

    def get_analysis(self):
        return self.sp.audio_analysis(self.uri)

