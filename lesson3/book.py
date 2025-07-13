class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def book_info(self):
        return f"Book: {self.title}, Author: {self.author}"