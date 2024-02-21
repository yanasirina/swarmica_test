from . import models


class BookIsNotAvailable(Exception):
    pass


def give_book_to_client(book: models.Book, client: models.Client) -> None:
    if not book.is_book_in_stock():
        raise BookIsNotAvailable('Нет свободных книг')
    models.HandedBook.objects.create(book=book, client=client)


def return_book_from_client(book: models.Book, client: models.Client) -> None:
    if not (handed_book := client.handed_books.filter(book=book).first()):
        raise BookIsNotAvailable('Клиент не брал выбранную книгу')
    handed_book.delete()
