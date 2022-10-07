class Msg: 
    def __init__(self):
        pass

    def search(self, iter, length):
        self.iter = iter 
        self.length = length 
        print("Searching: ", iter,"/", length)

    def save(self, file):
            self.file = file 
            print("Torrent found, saving: "+ file)

    def result(self, file):
            print("Torrent not on Blutopia")
            
