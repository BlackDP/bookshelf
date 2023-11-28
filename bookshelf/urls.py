from django.contrib import admin
from django.urls import path

from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', html_books_view),
    path('books/<int:book_id>/', html_book_view),
    path('api/books/', api_books_view),
    path('api/books/<int:book_id>/', get_api_book),
]
