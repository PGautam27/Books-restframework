from django.contrib import admin
from django.urls import path
from book_api.views import BookList, book_create, book
urlpatterns = [
    path('list/', BookList.as_view()),
    path('', book_create),
    path('<int:pk>', book)
]
