from rest_framework import serializers

from .fields import Base64ImageField
from .models import Book


class BookWriteSerializer(serializers.ModelSerializer):
    """Сериализатор ингредиентов для рецепта."""

    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Book
        fields = ('id', 'author', 'year', 'title', 'preface', 'image')


class BookReadSerializer(serializers.ModelSerializer):
    """Сериализатор ингредиентов для рецепта."""

    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ('id', 'author', 'year', 'title', 'preface', 'image')
