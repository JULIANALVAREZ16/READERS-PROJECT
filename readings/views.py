from django.shortcuts import render
from .models import Book
from rest_framework import viewsets
from .serializador import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
