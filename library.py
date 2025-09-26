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
        self._title = title
        self._author = author
        self._isbn = isbn
        self._total_copies = total_copies #сколько всего книг имеется

        self._available_copies = 0 #книги доступныве к выдаче. Когда выдаём книгу уменьшаем эту переменную и наоборот при получении книги обратно



class Reader: #Класс читателя
    def __init__(self, name, email):
        self._name = name
        self._email = email

        self._active_loans = None # книги которые находятся у читателя


class Library:
    def __init__(self):
        self._book_catalog = dict() #каталог книг
        # self.__magazine = magazine #журнал выдач

    def add_book(self, book, copies): #copies это сколько физических экземпляров пытаются добавить в библиотеку
        if not isinstance(book, Book):
            raise TypeError('Книга должна быть экземпляром класса Book')
        if not 0 < copies <= book._total_copies:
            raise ValueError('Попытка добавить в библиотеку книг больше чем выпущено ')
        if book._isbn in self._book_catalog:
            self._book_catalog[book._isbn]._available_copies += copies
        else:
            self._book_catalog[book._isbn] = book
            book._available_copies += copies

    def remove_book(self, isbn, copies):
        if not isbn in self._book_catalog and isinstance(isbn, int) and isinstance(copies, int):
            raise TypeError('Не верные аргументы')
        if copies <= 0:
            raise ValueError('Кол-во книг для удаления должно быть больше 0')
        book = self._book_catalog[isbn]
        if copies > book._available_copies:
            raise ValueError(f'Кол-во книг для удаления не должно превышать колличества книг готовых к выдаче : {book._available_copies}')
        book._available_copies -= copies
        print(f'{copies} экземпляров книг под номером {isbn} удалено из библиотеки')

    def borrow(self, isbn, reader): #выдача книги
        if not isbn in self._book_catalog and isinstance(reader, Reader) and isinstance(isbn, int):
            raise TypeError('Не верные аргументы')
        self._book_catalog[isbn]._available_copies -= 1
        if reader._active_loans == None:
            reader._active_loans = 1
        else:
            reader._active_loans += 1

    def return_book(self, isbn, reader):
        if not isbn in self._book_catalog and isinstance(reader, Reader) and isinstance(isbn, int):
            raise TypeError('Не верные аргументы')

        self._book_catalog[isbn]._available_copies += 1
        reader._active_loans -= 1


    def stock(self, isbn):
        if not isbn in self._book_catalog:
            raise ValueError('Такого isbn в каталоге книг не существует')

        print(f'Всего книг под номером {isbn}: {self._book_catalog[isbn]._total_copies}')
        print(f'Доступно для выдачи книг под номером {isbn}: {self._book_catalog[isbn]._available_copies}')



    def find(self, query):
        found_book = None
        for isbn, book in self._book_catalog.items():
            if book._title == query:
                found_book = book
            else:
                return 'Книга не найдена'
        return found_book
