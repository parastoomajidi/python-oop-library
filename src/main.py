from book import Book
from library import Library

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
# print(book1)
# print(book2)
my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)

my_library.list_book()