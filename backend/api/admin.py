from django.contrib import admin

from .models import (
    Author,
    Book
)


admin.site.empty_value_display = 'Не задано'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'date_of_birth',
        'autobiography'
    )
    search_fields = (
        'full_name',
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'year',
        'preface',
        'image'
    )
    search_fields = (
        'title',
        'author',
        'year'
    )
    list_filter = (
        'author',
        'year',
    )
    list_display_links = (
        'title',
    )
    