from django.shortcuts import render
from .models import Author, Book

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author.html', {'authors': authors})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'book': books})
