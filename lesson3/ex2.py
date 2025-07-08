from book import Book

library = [
    Book ("Елена Звездная", "Академия проклятий"),
    Book ("Надежда Кузьмина", "Наследница драконов"),
    Book ("Арем Каменистый", "Практикантка")
]


for book in library:
    print (f"{book.title} - {book.author}")