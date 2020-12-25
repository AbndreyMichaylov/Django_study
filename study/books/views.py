from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author
from .serializers import BooksSerializer

class BooksView(APIView):

    def get(self, request):
        
        books = Author.objects.filter(first_name__startswith = 't')
        serializer = BooksSerializer(books, many=True)
        return Response({"books":serializer.data})
        