from rest_framework.views import APIView
from rest_framework.response import Response
from library.models.author import Author
from library.serializers.author_serializer import AuthorSerializer

class AuthorListView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
