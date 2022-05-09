from django.shortcuts import render
from book_api.models import Book


# Create your views here.
def book_list(request):
    books = Book.objects.all()
