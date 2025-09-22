# 1) Библиотека
#
# Классы: Book, Reader, Library.
# Требования:
#
# Book: title, author, copies.
#
# Reader: name, email.
#
# Library: books (каталог), методы add_book(book), borrow(book, reader), return_book(book, reader).
# Проверки: нельзя выдать, если нет доступных копий; возврат — только если эта пара «reader↔book» существует.
# Инварианты: copies >= 0.
# Усложнение: лимит активных книг на читателя; штрафы за просрочку (пока без дат — счётчиком дней).


# 1) Библиотека
#
#Сущности: Book, Reader, Library.

#TODO Атрибуты: Book: title, author, isbn, total_copies, available_copies.
# Reader: name, email, active_loans (множество ISBN/экземпляров).
# Library: каталог книг (по ISBN), журнал выдач.
#
#TODO Методы (обязательные):
# Library.add_book(book, copies) — увеличить общий и доступный фонд.
# Library.remove_book(isbn, copies) — уменьшить фонд (нельзя уйти ниже активных выдач).
# Library.borrow(isbn, reader) — выдать 1 экз., уменьшить available_copies, записать в active_loans.
# Library.return_book(isbn, reader) — вернуть, увеличить available_copies, снять из active_loans.
# Library.stock(isbn) — доступ/всего.
# Library.find(query) — поиск по названию/автору.
#
#TODO Проверки/ошибки: нет доступных копий; возврат невыданной книги; отрицательные аргументы; дублирующая выдача.
#
#TODO Инварианты: 0 ≤ available_copies ≤ total_copies.
#
#TODO Усложнения: лимит активных книг на читателя; «штрафной счётчик дней»; бронирование.

class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies #сколько всего книг имеется

        self.available_copies = 0 #книги доступныве к выдаче. Когда выдаём книгу уменьшаем эту переменную и наоборот при получении книги обратно



class Reader: #Класс читателя
    def __init__(self, name, email, active_loans):
        self.name = name
        self.email = email
        self.active_loans = active_loans # книги которые находятся у читателя


class Library:
    def __init__(self, book_catalog, magazine):
        self.book_catalog = list(book_catalog) #каталог книг
        self.magazine = magazine #журнал выдач

    def add_book(self, book, copies): #copies это сколько физических экземпляров пытаются добавить в библиотеку
        if copies > book.total_copies and copies > 0:
            raise ValueError('Попытка добавить в библиотеку книг больше чем выпущено ')
        self.book_catalog.append(book)
        book.available_copies += copies


    def remove_book(self, isbn, copies):
        pass



    def borrow(self, isbn, copies):
        pass #выдача книги


    def return_book(self, isbn, reader):
        pass


    def stock(self, isbn):
        pass


    def find(self, query):
        pass