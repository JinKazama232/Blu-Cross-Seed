import pandas as pd
import imp
import csv
import os
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
from urllib import request 
import _config
imp.reload(_config)
import helpers
imp.reload(helpers)

m = helpers.Msg()

### Generate file list
upload_list = pd.DataFrame()
paths = _config.media_folders

upload_list = helpers.create_file_list(paths, upload_list)

for i in range(len(upload_list)):
    time.sleep(_config.api_delay)
    print(m.search(i, len(upload_list)))
    params = {
        'api_token' : _config.token,
        'file_name' : upload_list.iloc[i, 0]
    }
    
    response = requests.get(_config.search_url, params=params)
    response = response.json()
    
    if len(response['data']) == 0:
        print("Torrent not on Blutopia")
        continue

    else: 
        torrent_file = upload_list.iloc[i, 0] + '.torrent'
        url = response["data"][0]["attributes"]["download_link"]
        os.chdir(_config.output_folder)
        response_dl = request.urlretrieve(url, torrent_file)
        print(m.save(torrent_file))
