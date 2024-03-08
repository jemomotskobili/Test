import json

class Book:
    def __init__(self, title, author, year):
        # წიგნის ინიციალიზაცია , სახელით , ავტორით , გამოწვეყნების წელით
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        
        return f"'{self.title}' by {self.author}, {self.year}"

class BookManager:
    def __init__(self, filename='books.json'):
        
        self.books = []  # წიგნების ლისტი
        self.filename = filename  # json ფაილი წიგნების შესანახად
        self.load_books()  # წიგნების ჩატვირთვ json ფაილიდან

    def add_book(self, book):
        # წიგნის დამატება და შენახვა
        self.books.append(book)
        self.save_books()

    def show_books(self):
        # ყველა წიგნის დაბეჭდვა
        for book in self.books:
            print(book)

    def search_books(self, title):
        # წიგნის ძიება სათაურის მიხედვით
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def save_books(self):
        # წიგნის შენახვა
        with open(self.filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)

    def load_books(self):
        # წიგნის ჩატვირთვა  
        try:
            with open(self.filename, 'r') as f:
                books_data = json.load(f)
                for book_data in books_data:
                    self.books.append(Book(**book_data))
        except FileNotFoundError:
            # ცარიელი წიგნების სია
            self.books = []

def main():
    
    manager = BookManager()

    while True:
        # მენიუ დაბეჭდვა
        print("\nMenu")
        print("1. Add a new book")
        print("2. Show all books")
        print("3. Search for a book")
        print("4. Exit")
        choice = input("Enter your choice: ")
          #მენიუს ღილაკები
        if choice == "1":
            
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter publication year: ")

            # წიგნის დამატების ვალიდაცია
            if not title or not author or not year.isdigit():
                print("Invalid input. Please try again.")
                continue

            book = Book(title, author, int(year))
            manager.add_book(book)
            print("Book added successfully.")

        elif choice == "2":
            
            print("\nList of all books:")
            manager.show_books()

        elif choice == "3":
            
            search_title = input("Enter book title to search: ")
            found_books = manager.search_books(search_title)
            if found_books:
                print("\nFound Books:")
                for book in found_books:
                    print(book)
            else:
                print("No books found with that title.")

        elif choice == "4":
            
            print("Exiting program.")
            break

        else:
            
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()