import os
from book import Book
from library import Library

def run_new():
    title= input("please enter the book name: ")
    author= input ("please enter the author name: ")
    isbn = input("plese enter the isbn number of book: ")
    my_library = Library()
    new_book = Book(title, author, isbn)
    my_library.add_book(new_book)
    my_library.find_book_by_isbn(new_book)

    # write in file
    saveFile = "books.txt"
    with open (saveFile, "a") as f:
        f.write(f"{title}, {author}, {isbn}\n")

# menu
menu = int(input("Choose:\n 1-add book,\n 2-show list,\n 3-exit\n "))

if menu == 1:
    run_new()

elif menu == 2:
    if not os.path.exists("books.txt"):
        print("📂 No books found! The library is empty.")
    else:
        with open("books.txt") as f:
            lines = f.read().splitlines()

        print("\n📚 Book List:")
        for line in lines:
            print(line)

else:
    exit()
