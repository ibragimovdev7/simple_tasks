class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)
        print(f'Add the {book}')

    def remove(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'Removed the {book} in my list')
        else:
            print(f'{book} not found')

    def search_with_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            print(f'{author} books:')
            for book in found_books:
                print(book)
        else:
            print(f"{author}'s book not found.")

    def search_with_year(self, year):
        found_books = [book for book in self.books if book.year == year]
        if found_books:
            print(f'{year} books:')
            for book in found_books:
                print(book)
        else:
            print(f"{year}'s book not found.")


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.name}      {self.year}       {self.author}'


a = [
    Book("Sherlock Holmes", "Sir Arthur Conan Doyle", 1892),
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960)
]

l1 = Library()
for i in a:
    l1.add(i)
