# Author data access logic here
# Author data access logic here
from library.models import Author

class AuthorRepository:
    @staticmethod
    def get_all():
        return Author.objects.all()

    @staticmethod
    def get_by_id(author_id):
        return Author.objects.filter(id=author_id).first()

    @staticmethod
    def create(**kwargs):
        return Author.objects.create(**kwargs)
