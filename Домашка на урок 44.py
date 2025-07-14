class library:
    def __init__(self):
        self.books = []


    def add_book(self , book):
        self.books.append(book)


    def remove_book(self , book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Ошибка")


    def find_book(self , book):
        return book in self.books
        self.books


    def print_book(self):
        if not self.books:
            print("Список пуст")
        else:
            for i in range(len(self.books)):
                print(f"{self.books[i]}:{i}")


bohh = library()
bohh.add_book("300 спартанцев")
bohh.add_book("Древний рим")
bohh.add_book("Все про Египет")
bohh.add_book("Куликовская битва")

print(bohh.print_book())

print(bohh.find_book("300 спартанцев"))
print(bohh.find_book("Все про пиццу"))

print(bohh.remove_book("300 спартанцев"))
print(bohh.remove_book("Все про пиццу"))
print(bohh)


