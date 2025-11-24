import json
import logging
from .book import Book



logging.basicConfig(filename="library.log", level=logging.INFO)

class LibraryInventory:
    def __init__(self, filepath="catalog.json"):
        self.filepath = filepath
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)
                self.books = [Book(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            logging.error("Catalog file missing or corrupted — starting empty.")
            self.books = []

    def save_data(self):
        with open(self.filepath, "w") as file:
            json.dump([b.to_dict() for b in self.books], file, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return self.books
