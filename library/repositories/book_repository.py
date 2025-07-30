
# Book data access logic here
from library.models import Book

class BookRepository:
    @staticmethod
    def get_all():
        return Book.objects.select_related("author").all()

    @staticmethod
    def get_by_id(book_id):
        return Book.objects.filter(id=book_id).first()

    @staticmethod
    def create(**kwargs):
        return Book.objects.create(**kwargs)
