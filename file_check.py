import pandas as pd
import csv
import pickle
import os
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
from urllib import request 

search_url = 'https://blutopia.xyz/api/torrents/filter'
torrent_url = 'https://blutopia.xyz/api/torrents/'
upload_url = 'https://blutopia.xyz/api/torrents/upload' 
delay = 20
### Generate file list
upload_list = pd.DataFrame()
paths = (r'H:\\Movies', r'G:\\Movies', r'G:\\xSeed\\PTP')

for i in range(len(paths)):

    file_list = os.listdir(paths[i])
    upload_list = upload_list.append(file_list)


for i in range(len(upload_list)):
    time.sleep(delay)
    print("Searching: ", i,"/", len(upload_list))
    params = {
        'api_token' : "fCYiRFERR0IhtD3wwvQIJRov8IlfjdEi5lU8CRID4NH1JM2IAmVsd9DW8PZXdhckruK6GnK9qCVu3TvPq39ihkq1CRElMU4bUaSZ",
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
        os.chdir("C:\\Users\\zbyni\\AppData\\Local\\Blu-Uploads")
        response_dl = request.urlretrieve(url, torrent_file)
        print("Torrent found, saving: "+ torrent_file)
