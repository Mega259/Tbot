import json
import os

class Parameters():
    def __init__(self):
        self.get_access_data()
    
    def get_access_data(self):
        path_folder = os.path.abspath(os.path.dirname(__file__))
        path_data = os.path.join(path_folder, 'access_data.json')
        with open(path_data, 'r') as f:
            access_data = json.load(f)
            f.close()
        self.__token = access_data['token']
        self.__endpoint = access_data['endpoint']
    
    def get_token(self):
        return self.__token

    def get_endpoint(self):
        return self.__endpoint