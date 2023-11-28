from django.contrib import admin
from django.urls import path

from books.views import html_books_view, html_book_view, api_books_view, api_book_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', html_books_view),
    path('books/<int:book_id>/', html_book_view),
    path('api/books/', api_books_view),
    path('api/books/<int:book_id>/', api_book_view),
]
