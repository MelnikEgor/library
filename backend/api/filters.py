from django_filters import rest_framework as filters_dj

from .models import Book


class BookFilter(filters_dj.FilterSet):
    author = filters_dj.CharFilter(
        field_name='author__full_name',
        lookup_expr='icontains'
    )
    year = filters_dj.NumberFilter(field_name='year')

    class Meta:
        model = Book
        fields = ['year', 'author']
