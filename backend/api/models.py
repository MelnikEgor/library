from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.timezone import now


class Author(models.Model):
    full_name = models.CharField(
        'ФИО',
        max_length=128,
    )
    date_of_birth = models.DateField(
        'Дата рождения',
    )
    autobiography = models.TextField(
        'Автобиография',
        blank=True,
    )

    class Meta():
        verbose_name = 'автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.full_name}'


class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Автор книги'
    )
    year = models.PositiveSmallIntegerField(
        'Год издания',
        validators=[
            MaxValueValidator(
                now().year,
                'Год издания не может быть больше текущего.'
            ),
        ]
    )
    title = models.CharField(
        'Название',
        max_length=128
    )
    preface = models.TextField(
        verbose_name='Предисловие',
        blank=True,
    )
    image = models.ImageField(
        'Изображение',
        upload_to='images/',
        blank=True
    )

    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        default_related_name = 'books'

    def __str__(self):
        return f'{self.title}'
