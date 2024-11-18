class Book:
    def __init__(self, title, author, year, genre, status=False) -> None:
        if not title or not isinstance(title, str):
            raise ValueError("Title must be a non-empty string.")
        if not author or not isinstance(author, str):
            raise ValueError("Author must be a non-empty string.")
        if not isinstance(year, int) or year < 1000 or year > 9999:
            raise ValueError("Year must be a valid four-digit integer.")
        if not genre or not isinstance(genre, str):
            raise ValueError("Genre must be a non-empty string.")

        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.status = status
    
    def mark_as_rented(self):
        if not self.status:
            self.status = True
        else:
            return f"Book '{self.title}' is already rented"

    def mark_as_available(self):
        if self.status:
            self.status = False
        else:
            print("Book is already available")

class User:
    def __init__(self, username, user_id) -> None:
        if not username or not isinstance(username, str):
               raise ValueError("Username must be a non-empty string.")
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("User ID must be a positive integer.")

        self.username = username
        self.user_id = user_id
        self.rented_books = []

    def rent_book(self, book):
        if book.status:  
            print(f"The book '{book.title}' is already rented.")
        else:
            book.mark_as_rented() 
            self.rented_books.append(book) 


    def return_book(self, book):
        if book in self.rented_books:
            self.rented_books.remove(book)
            book.mark_as_available()
        else:
            print(f"{self.username} does not have the book: {book.title}")

class Library:
    def __init__(self, books=None, users=None) -> None:
        self.books = books if books else []
        self.users = users if users else []
    
    def add_book(self, book):
        if not any(book.title == existing_book.title for existing_book in self.books):
            self.books.append(book)
        else:
            print(f"Book '{book.title}' is already in the library")

    def register_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"User '{user.username}' added")
        else:
            print(f"User '{user.username}' is already registered")

    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books:
            if  (title and title.lower() in book.title.lower()) or \
                (author and author.lower() in book.author.lower()) or \
                (genre and genre.lower() in book.genre.lower()):
                results.append(book)
        return results

class RentalSystem:
    def __init__(self, library) -> None:
        self.library = library

    def rent_book_to_user(self, user, book):
        user.rent_book(book)

    def return_book_from_user(self, user, book):
        user.return_book(book)