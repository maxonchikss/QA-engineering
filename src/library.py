class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []

    def add_book(self, title: str):
        self.available_books.append(title)

    def borrow_book(self, title: str):
        if title not in self.available_books:
            raise ValueError("Book is not available or does not exist")
        self.available_books.remove(title)
        self.borrowed_books.append(title)

    def return_book(self, title: str):
        if title not in self.borrowed_books:
            raise ValueError("Book was not borrowed and cannot be returned")
        self.borrowed_books.remove(title)
        self.available_books.append(title)

    def is_book_available(self, title: str) -> bool:
        return title in self.available_books

    def get_total_books(self) -> int:
        return len(self.available_books) + len(self.borrowed_books)
