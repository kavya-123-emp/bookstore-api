# Business logic for book here
# Business logic for book here
from library.models import Book

class BookService:
    @staticmethod
    def get_all_books():
        return Book.objects.select_related("author").all()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.objects.filter(id=book_id).first()

    @staticmethod
    def create_book(data):
        return Book.objects.create(**data)

    @staticmethod
    def update_book(book, data):
        for key, value in data.items():
            setattr(book, key, value)
        book.save()
        return book

    @staticmethod
    def delete_book(book):
        book.delete()
