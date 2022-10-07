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

    def result(self):
            return "Torrent not on Blutopia"
            
