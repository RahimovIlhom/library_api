from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers

from .models import Book


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'sub_title', 'author', 'price', 'isbn']

    def validate(self, data):
        title: str = data.get('title')
        author = data.get('author')
        if title.isdigit():
            raise ValidationError("Titleda xatolik")
        if Book.objects.filter(title=title, author=author):
            raise ValidationError("Bu kitob qo'shilgan")
        return data

    def validate_price(self, price):
        if 0 > price or price > 9999999:
            raise ValidationError("Narx xato")
        return price


# class BookSerializer(Serializer):
#     title = serializers.CharField(max_length=255)
#     body = serializers.CharField()
#     price = serializers.IntegerField()
#
#     class Meta:
#         fields = ['title', 'body', 'price']
