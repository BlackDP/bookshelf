from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from .models import Book
# Create your views here.


def get_books():
    books = Book.objects.all()
    return books

def get_book(book_id: int):
    try:
        book = Book.objects.get(id=book_id)
        return book
    except:
        return None

def html_books_view(request):
    books = get_books()
    return render(request, 'books/books.html', context={'books':books})

def html_book_view(request, book_id: int):
    book = get_book(book_id)
    if book is None:
        return HttpResponseNotFound()
    return render(request, 'books/book.html', context={'book':book})

def api_books_view(request):
    books = get_books()
    books = list(books.values('title', 'author_full_name', 'year_of_publishing', 'copies_printed', 'short_description'))
    return JsonResponse(books, safe=False, json_dumps_params={'ensure_ascii': False})

def get_api_book(request, book_id: int):
    book = get_book(book_id)
    if book is None:
        return HttpResponseNotFound()
    return JsonResponse({
        'title': book.title,
        'author_full_name': book.author_full_name,
        'year_of_publishing': book.year_of_publishing,
        'copies_printed': book.copies_printed,
        'short_description': book.short_description,
    }, json_dumps_params={'ensure_ascii': False})