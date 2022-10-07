import pandas as pd
import csv
import pickle
import os
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time

search_url = 'https://blutopia.xyz/api/torrents/filter'
torrent_url = 'https://blutopia.xyz/api/torrents/'
upload_url = 'https://blutopia.xyz/api/torrents/upload' 
delay = 20
### Generate file list
upload_list = pd.DataFrame()
path = 'G:\\xSeed\\PTP'
file_list = os.listdir(path)

for i in range(len(file_list)):
### Select file_list
    time.sleep(delay)
    selected_file = file_list[i]
    print("[",i,"/",len(file_list),"] Now checking:", selected_file)
    if os.path.isfile(path + "\\" + selected_file):
        movie_file = selected_file 

        #### Modifying file name ###
        #movie_file = "The.Grifters.1990.720p.BluRay.DTS.x264-Skazhutin.mkv"
        movie_file = movie_file.split('.mkv')[0]
        movie_file = movie_file.split('.mp4')[0]
        movie_file = movie_file.replace(".", " ")
        movie_file = movie_file.replace("&", " & ")
        
        #Codec
        movie_file = movie_file.replace("H264", "H.264")
        movie_file = movie_file.replace("H265", "H.265")
        movie_file = movie_file.replace("H 264", "H.264")
        movie_file = movie_file.replace("H 265", "H.265")
        #Audio
        movie_file = movie_file.replace("AC3", "DD")
        movie_file = movie_file.replace("EAC3", "DDP")
        movie_file = movie_file.replace("FLAC1 0", "FLAC 1.0")
        movie_file = movie_file.replace("FLAC2 0", "FLAC 2.0")
        
        movie_file = movie_file.replace("DDP5 1", "DD+ 5.1")
        movie_file = movie_file.replace("DDP2 0", "DD+ 2.0")
        movie_file = movie_file.replace("DDP3 0", "DD+ 3.0")
        movie_file = movie_file.replace("DDP7 1", "DD+ 7.1")
        
        movie_file = movie_file.replace("DTS5 1", "DTS 5.1")
        movie_file = movie_file.replace("DTS2 0", "DTS 2.0")
        movie_file = movie_file.replace("DTS3 0", "DTS 3.0")
        movie_file = movie_file.replace("DTS7 1", "DTS 7.1")
        
        movie_file = movie_file.replace("AAC5 1", "AAC 5.1")
        movie_file = movie_file.replace("AAC2 0", "AAC 2.0")
        movie_file = movie_file.replace("AAC3 0", "AAC 3.0")
        movie_file = movie_file.replace("AAC7 1", "AAC 7.1")
        movie_file = movie_file.replace("AAC1 0", "AAC 1.0")
        
        movie_file = movie_file.replace("DD+5 1", "DD+ 5.1")
        movie_file = movie_file.replace("DD+2 0", "DD+ 2.0")
        movie_file = movie_file.replace("DD+3 0", "DD+ 3.0")
        movie_file = movie_file.replace("DD+7 1", "DD+ 7.1")
        
        movie_file = movie_file.replace("DD5 1", "DD 5.1")
        movie_file = movie_file.replace("DD2 0", "DD 2.0")
        movie_file = movie_file.replace("DD3 0", "DD 3.0")
        movie_file = movie_file.replace("DD7 1", "DD 7.1")
        
        movie_file = movie_file.replace("5 1", "5.1")
        movie_file = movie_file.replace("1 0", "1.0")
        movie_file = movie_file.replace("2 0", "2.0")
        movie_file = movie_file.replace("3 0", "3.0")
        movie_file = movie_file.replace("7 1", "7.1")
        
        movie_file = movie_file.replace(".1080p", " 1080p")
        movie_file = movie_file.replace(".720p", " 720p")
        movie_file = movie_file.replace(".2160p", " 2160p")
        
        
        if "720p" in movie_file:
            movie_quality = "720p"
        elif "1080p" in movie_file:
            movie_quality = "1080p"   
        elif "2160p" in movie_file:
            movie_quality = "2160p"
        else:
            continue
        
        if "WEB" in movie_file:
            movie_type = "WEB"
            movie_gen = movie_file.split(movie_quality)[0]
            params2 = {
                'api_token' : "fCYiRFERR0IhtD3wwvQIJRov8IlfjdEi5lU8CRID4NH1JM2IAmVsd9DW8PZXdhckruK6GnK9qCVu3TvPq39ihkq1CRElMU4bUaSZ",
                'name' : movie_gen + movie_quality + ' WEB',
            }
            params = {
                'api_token' : "fCYiRFERR0IhtD3wwvQIJRov8IlfjdEi5lU8CRID4NH1JM2IAmVsd9DW8PZXdhckruK6GnK9qCVu3TvPq39ihkq1CRElMU4bUaSZ",
                'name' : movie_file,
            }
        
          
            response2 = requests.get(search_url, params=params2)
            response2 = response2.json()
            
            if len(response2['data']) == 0:
                print('This WEBDL is not uploaded')
                print('No', movie_quality, 'WEBDL uploaded - Adding to the list')
                status = "Not a dupe"
               
            else:
                status = "Dupe"
                print('Dupe')
                 
        elif "REMUX" in movie_file:
            movie_type = "REMUX"   
            movie_gen = movie_file.split(movie_quality)[0]
            movie_gen = movie_gen.split('BluRay')[0]
            movie_gen = movie_gen.split('Blu-Ray')[0]
            movie_gen = movie_gen.split('HDDVD')[0]
            movie_gen = movie_gen.split('HD-DVD')[0]
            params2 = {
                'api_token' : "fCYiRFERR0IhtD3wwvQIJRov8IlfjdEi5lU8CRID4NH1JM2IAmVsd9DW8PZXdhckruK6GnK9qCVu3TvPq39ihkq1CRElMU4bUaSZ",
                'name' : movie_gen + movie_quality + ' REMUX',
            }
            params = {
                'api_token' : "fCYiRFERR0IhtD3wwvQIJRov8IlfjdEi5lU8CRID4NH1JM2IAmVsd9DW8PZXdhckruK6GnK9qCVu3TvPq39ihkq1CRElMU4bUaSZ",
                'name' : movie_file,
            }
        
            response = requests.get(search_url, params=params)
            response = response.json()
            
            response2 = requests.get(search_url, params=params2)
            response2 = response2.json()
            
            if len(response['data']) == 0:
                print('This remux is not uploaded')
                if len(response2['data']) == 0:
                    print('No REMUX uploaded - Adding to the list')
                    status = "Not a dupe"
                else:
                    print('A REMUX is already uploaded')
            else:
                status = "Dupe"
                print('Dupe')
            
            
        elif "x264" in movie_file:
            movie_type = "Encode"
            try:
                group = movie_file.split('x264-')[1]
            except Exception:
                group = movie_file.split('x264')[1] 
                    
            movie_gen = movie_file.split(movie_quality)[0]
            movie_gen = movie_gen.split('BluRay')[0]
            movie_gen = movie_gen.split('Blu-Ray')[0]
            movie_gen = movie_gen.split('HDDVD')[0]
            movie_gen = movie_gen.split('HD-DVD')[0]
            params = {
                'api_token' : "fCYiRFERR0IhtD3wwvQIJRov8IlfjdEi5lU8CRID4NH1JM2IAmVsd9DW8PZXdhckruK6GnK9qCVu3TvPq39ihkq1CRElMU4bUaSZ",
                'name' : movie_gen + movie_quality + " x264 " + group,
            }
            response = requests.get(search_url, params=params)
            response = response.json()
            
            if len(response['data']) == 0:
                status = "Not a dupe"
                print('This ENCODE is not uploaded')

            else:
                status = "Dupe"
                print('Dupe')
    
                
            
        elif "x265" in movie_file:
            movie_type = "Encode"
            try:
                group = movie_file.split('x265-')[1]
            except Exception:
                group = movie_file.split('x265')[1] 
            movie_gen = movie_file.split(movie_quality)[0]
            movie_gen = movie_gen.split('BluRay')[0]
            movie_gen = movie_gen.split('Blu-Ray')[0]
            movie_gen = movie_gen.split('HDDVD')[0]
            movie_gen = movie_gen.split('HD-DVD')[0]
            params = {
                'api_token' : "fCYiRFERR0IhtD3wwvQIJRov8IlfjdEi5lU8CRID4NH1JM2IAmVsd9DW8PZXdhckruK6GnK9qCVu3TvPq39ihkq1CRElMU4bUaSZ",
                'name' : movie_gen + movie_quality + " x265 " + group,
            }
            response = requests.get(search_url, params=params)
            response = response.json()
            
            if len(response['data']) == 0:
                status = "Not a dupe"
                print('This ENCODE is not uploaded')

            else:
                status = "Dupe"
                print('Dupe')
        
        command = "python upload.py " + path + "\\" + selected_file
        info = pd.DataFrame([[selected_file, movie_file, movie_type, movie_quality, status, command]])
        
        
    else: 
        print("This is a directory")
        continue 
    
    upload_list = upload_list.append(info)
    
    
upload_list.columns = ["File_Name", "Release", "Type", "Quality", "Status", "Command"]   
csv_name = 'bluUpload3.csv'
upload_list.to_csv(csv_name)  
