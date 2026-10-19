class Library:
    book_list = []

    @classmethod
    def add_book(cls, book):
        cls.book_list.append(book)

    @classmethod
    def search_book(cls, id):
        for book in cls.book_list:
            if book.get_book_id() == id:
                return book
        return None


class Book:
    def __init__(self, title, is_borrowed=False):
        self.__book_id = len(Library.book_list) + 1
        self.__title = title
        self.__is_borrowed = is_borrowed
        Library.add_book(self)

    def borrow(self):
        if self.__is_borrowed:
            print("This book is already borrowed.\n")
        else:
            self.__is_borrowed = True
            print(f"Successfully borrowed {self.__title}.\n")

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            print("Thank You.\n")
        else:
            print("This book isn't borrowed yet.\n")

    def get_book_id(self):
        return self.__book_id
    
    def get_book_title(self):
        return self.__title

    def show_book(self):
        print(f"Book ID : {self.__book_id}")
        print(f"Title : {self.__title}")
        if self.__is_borrowed:
            print("Already Borrowd.\n")
        else:
            print("Available for borrowing.\n")


class EBook(Book):
    def __init__(self, title, file_size):
        super().__init__(title)
        self.__file_size = file_size

    def show_book(self):
        print(f"Title : {self.get_book_title()}")
        print(f'Book Size : {self.__file_size}\n')
        

book1 = Book("Pride and Prejudice")
book2 = Book("Moby Dick")
book3 = Book("Frankenstein")
book4 = Book("The Odyssey")
book5 = Book("Alice in Wonderland")

e = EBook("Dracula", 5)


def asking_for_id():
    try:
        ID = int(input("Enter Book ID: "))
        return ID
    except ValueError:
        print("Invalid ID type, Please enter a number.")
        return None

while True:
    print("1. Search Book")
    print("2. Borrow book")
    print("3. Return book")
    print("4. Exit")

    option = input("Enter Option: ")
    print()
    if option == "1":
        print("1. View All Books.")
        print("2. View Any Books.")
        sub_option = input("Enter Option: ")
        print()
        if sub_option == "1":
            for book in Library.book_list:
                if not isinstance(book,EBook):
                    book.show_book()
                else:
                    print("EBOOKS:")
                    book.show_book()
        elif sub_option == "2":
            ID = asking_for_id()
            print()
            if ID is not None:
                book = Library.search_book(ID)
                if book is not None:
                    if not isinstance(book,EBook):
                        book.show_book()
                    else:
                        print("EBOOKS:")
                        book.show_book()
                else:
                    print("Invalid ID.\n")
        else:
            print("Invalid Option.\n")
    elif option == "2":
        ID = asking_for_id()
        print()
        if ID is not None:
            book = Library.search_book(ID)
            if book is None:
                print("Invalid ID.\n")
            else:
                book.borrow()

    elif option == "3":
        ID = asking_for_id()
        print()
        if ID is not None:
            book = Library.search_book(ID)
            if book is None:
                print("Invalid ID.\n")
            else:
                book.return_book()
    elif option == "4":
        break
    else:
        print("Invalid Option, Please Enter Again.")
