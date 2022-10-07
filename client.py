from torf import Torrent
import xmlrpc.client
import bencode
import os
import qbittorrentapi
from deluge_client import DelugeRPCClient, LocalDelugeRPCClient
import base64
from pyrobase.parts import Bunch
import errno
import asyncio
import ssl
import shutil
from src.console import console 

client_config = {"qbit_url" : "127.0.0.1",
                "qbit_port" : "8080",
                "qbit_user" : "admin",           
                "qbit_pass" : "reddress89"       
                }


      
qbt_client = qbittorrentapi.Client(host=client_config['qbit_url'],
                                   port=client_config['qbit_port'], 
                                    username=client_config['qbit_user'],
                                    password=client_config['qbit_pass'])

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)      


# display qBittorrent info
print(f'qBittorrent: {qbt_client.app.version}')
print(f'qBittorrent Web API: {qbt_client.app.web_api_version}')
for k,v in qbt_client.app.build_info.items(): print(f'{k}: {v}')

# retrieve and show all torrents
for torrent in qbt_client.torrents_info():
    print(f'{torrent.hash[-6:]}: {torrent.name} ({torrent.state})')

qbt_client.app_preferences()

torrent_path  = 'D:\\Code\\Repos\\Upload-Assistant\\Lost.in.America.1985.1080p.BluRay.FLAC.1.0.x264-BabyRed.torrent'
save_dir = 'H:\\Movies\\iTS'
qbt_client.torrents_add(torrent_files = torrent_path, use_auto_torrent_management = False, is_skip_checking=True, save_path = save_dir, content_layout='Original')