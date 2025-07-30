# Business logic for author here
# Business logic for author here
from library.models import Author

class AuthorService:
    @staticmethod
    def get_all_authors():
        return Author.objects.all()

    @staticmethod
    def get_author_by_id(author_id):
        return Author.objects.filter(id=author_id).first()

    @staticmethod
    def create_author(data):
        return Author.objects.create(**data)

    @staticmethod
    def update_author(author, data):
        for key, value in data.items():
            setattr(author, key, value)
        author.save()
        return author

    @staticmethod
    def delete_author(author):
        author.delete()
