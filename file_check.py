import pandas as pd
import csv
import pickle
import os
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
from urllib import request 
from config import *

search_url = 'https://blutopia.xyz/api/torrents/filter'
torrent_url = 'https://blutopia.xyz/api/torrents/'
upload_url = 'https://blutopia.xyz/api/torrents/upload' 
### Generate file list
upload_list = pd.DataFrame()
paths = media_folders

for i in range(len(paths)):

    file_list = os.listdir(paths[i])
    upload_list = upload_list.append(file_list)


for i in range(len(upload_list)):
    time.sleep(api_delay)
    print("Searching: ", i,"/", len(upload_list))
    params = {
        'api_token' : token,
        'file_name' : upload_list.iloc[i, 0]
    }
    
    response = requests.get(search_url, params=params)
    response = response.json()
    
    if len(response['data']) == 0:
        print("Torrent not on Blutopia")
        continue

    else: 
        torrent_file = upload_list.iloc[i, 0] + '.torrent'
        url = response["data"][0]["attributes"]["download_link"]
        os.chdir(output_folder)
        response_dl = request.urlretrieve(url, torrent_file)
        print("Torrent found, saving: "+ torrent_file)
