
from item import Item

class Book(Item):
    def __init__(self, code, title, description, category, picture, quantityInStock, price, isbn, author, synopsis):
        super().__init__(code, title, description, category, picture, quantityInStock, price)
        self.isbn = isbn
        self.author = author
        self.synopsis = synopsis

    def preview(self):
        return self.synopsis


book1 = Book('B001', 'The Great Gatsby', 'A novel by F. Scott Fitzgerald', 'Fiction', 'book1.jpg', 10, 12.99, '978-0743273565', 'F. Scott Fitzgerald', 'A young man tries to win back his lost love.')

print(book1.title)
print(book1.viewFullDescription())
print(book1.preview())