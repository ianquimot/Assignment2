from item import Item

class DVD(Item):
    def __init__(self, code, title, description, category, picture, quantityInStock, price, director, certificate, listOfActor):
        super().__init__(code, title, description, category, picture, quantityInStock, price)
        self.director = director
        self.certificate = certificate
        self.listOfActor = listOfActor

dvd1 = DVD('D001', 'The Shawshank Redemption', 'A movie by Frank Darabont', 'Drama', 'dvd1.jpg', 5, 9.99, 'Frank Darabont', 'certificate nito', 'Tim Robbins, Morgan Freeman')
print('Title:', dvd1.title)
print('Actors:', dvd1.listOfActor)