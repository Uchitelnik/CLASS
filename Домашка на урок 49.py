class Book:
    def __init__(self, title , author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} ,а Автор: {self.author}"



class Library:
    def __init__(self):
        self.books = []

    def add_book(self , book):
        self.books.append(book)
        return f"Книга {book} успешно добавлена "


    def list_book(self):
         if not self.books:
             return "В библиотеке пусто"
         else:
             return self.books


library = Library()

book1 = Book("Властелин Колец" ,"Толкиен")
book2 = Book("Детсво" , "Лев Толстой")


print(library.add_book(book1))
print(library.add_book(book2))

print(library.list_book())