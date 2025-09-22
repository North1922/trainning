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
        self.book_catalog = dict(book_catalog) #каталог книг
        self.magazine = magazine #журнал выдач

    def add_book(self, book, copies): #copies это сколько физических экземпляров пытаются добавить в библиотеку
        if book.total_copies > copies > 0:
            raise ValueError('Попытка добавить в библиотеку книг больше чем выпущено ')
        if book.isbn in self.book_catalog:
            self.book_catalog[book.isbn].available_copies += copies
        else:
            self.book_catalog[book.isbn] = book
            book.available_copies += copies

    def remove_book(self, isbn, copies):
        if copies <= 0:
            raise ValueError('Кол-во книг для удаления должно быть больше 0')
        book = self.book_catalog[isbn]
        book.available_copies -= copies
        print(f'{copies} экземпляров книг под номером {isbn} удалено из библиотеки')

    def borrow(self, isbn, reader): #выдача книги
        for book in self.book_catalog:
            if book.isbn == isbn:
                book.available_copies -= 1
                reader.active_loans += 1

    def return_book(self, isbn, reader):
        for book in self.book_catalog:
            if book.isbn == isbn:
                book.available_copies += 1
                reader.active_loans -= 1


    def stock(self, isbn):
        for book in self.book_catalog:
            if book.isbn == isbn:
                print(f'Всего книг под номером {isbn}: {book.total_copies}')
                print(f'Доступно для выдачи книг под номером {isbn}: {book.available_copies}')



    def find(self, query):
        found_book = None
        for book in self.book_catalog:
            if book.title == query:
                found_book = book
            else:
                return 'Книга не найдена'
        return found_book