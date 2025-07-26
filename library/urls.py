# URL routing for views
from django.urls import path
from library.views.author_view import AuthorListView
from library.views.book_view import BookListView

urlpatterns = [
    path('authors/', AuthorListView.as_view()),
    path('books/', BookListView.as_view()),
]
