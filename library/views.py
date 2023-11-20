from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer


# @api_view(['GET'])
# def book_list_api_view(request):
#     books = Book.objects.all()
#     serializers = BookSerializer(books, many=True)
#     return Response(serializers.data)


# class BooksListAPiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookRetrieveApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# Optimal Views ------------------------------------------------

# class BookListCreateApiView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
# ----------------------------------------------------------------


# APIViews

class BookListCreateApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        data = {
            'status': True,
            'count': f"{len(books)} ta kitoblar mavjud",
            'books': serializer.data
        }
        return Response(data)

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'status': True,
                'book': data
            })


# class BookRetrieveUpdateDeleteApiView(APIView):
#     def get(self, request, pk):
#         try:
#             book = Book.objects.get(id=pk)
#             serializer = BookSerializer(book)
#             data = {
#                 'status': True,
#                 'data': serializer.data
#             }
#             return Response(data, status=status.HTTP_200_OK)
#         except Book.DoesNotExist:
#             return Response({
#                 'status': False,
#                 'message': 'Book not found'
#             }, status=status.HTTP_404_NOT_FOUND)


class BookRetrieveUpdateDeleteApiView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        serializer = BookSerializer(instance=book)
        return Response({
            'status': 'success',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            'status': True,
            'data': serializer.data,
        })

    def delete(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        # serializer = BookSerializer(instance=book)
        # serializer.delete()
        book.delete()
        return Response({
            'status': True,
            'message': "Book deleted",
        })
# ------------------------------------------------------------------------

# Viewsets


class BookListApiView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
