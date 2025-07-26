from rest_framework.views import APIView
from rest_framework.response import Response
from library.models.book import Book
from library.serializers.book_serializer import BookSerializer

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
