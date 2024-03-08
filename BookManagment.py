import json

class Book:
    def __init__(self, title, author, year):
        # Initialize a Book instance with title, author, and publication year.
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # String representation of the Book instance.
        return f"'{self.title}' by {self.author}, {self.year}"

class BookManager:
    def __init__(self, filename='books.json'):
        # Initialize the BookManager, loading books from a JSON file.
        self.books = []  # List to store Book instances.
        self.filename = filename  # JSON file for storing books data.
        self.load_books()  # Load books from the JSON file.

    def add_book(self, book):
        # Add a Book instance to the manager and save to JSON file.
        self.books.append(book)
        self.save_books()

    def show_books(self):
        # Print all books in the manager.
        for book in self.books:
            print(book)

    def search_books(self, title):
        # Search for books by title (case-insensitive).
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def save_books(self):
        # Save the list of books to a JSON file.
        with open(self.filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)

    def load_books(self):
        # Load books from the JSON file.
        try:
            with open(self.filename, 'r') as f:
                books_data = json.load(f)
                for book_data in books_data:
                    self.books.append(Book(**book_data))
        except FileNotFoundError:
            # If no JSON file exists, start with an empty book list.
            self.books = []

