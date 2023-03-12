
from item import Item

class MP3(Item):
    def __init__(self, code, title, description, category, picture, quantityInStock, price, duration, artist):
        super().__init__(code, title, description, category, picture, quantityInStock, price)
        self.duration = duration
        self.artist = artist
    
    def playExtract(self):
        return self.playExtract

    def download(self):
        return self.download


mp3_1 = MP3('M001', 'Bohemian Rhapsody', 'A song by Queen', 'Rock', 'mp3_1.jpg', 100, 0.99, '6 minutes', 'Bohemian Rhapsody')

print('Title:', mp3_1.title)
print('Duration:', mp3_1.duration)