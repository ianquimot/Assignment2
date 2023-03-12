
class Item:
    def __init__(self, code, title, description, category, picture, quantityInStock, price):
        self.code = code
        self.title = title
        self.description = description
        self.category = category
        self.picture = picture
        self.quantityInStock = quantityInStock
        self.price = price
    
    def viewFullDescription(self):
        return self.description
    
    def addToCart(self):
        return self.addToCart
    
    def updateStockLevel(self, new_quantity):
        self.updateStockLevel = new_quantity
