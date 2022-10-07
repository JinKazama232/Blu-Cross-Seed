import os

class Msg: 
    def __init__(self):
        pass

    def search(self, iter, length):
        self.iter = iter 
        self.length = length 
        return "Searching: ", iter,"/", length

    def save(self, file):
            self.file = file 
            "Torrent found, saving: "+ file

def create_file_list(path, upload_list):
    for i in range(len(path)):
        file_list = os.listdir(path[i])
        upload_list = upload_list.append(file_list)
    return upload_list