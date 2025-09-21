from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from .filters import BookFilter
from .models import (
    Book
)
from .permissions import IsSuperUserOrReadOnly
from .serializers import BookReadSerializer, BookWriteSerializer


class BookViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """Представление книги."""

    queryset = Book.objects.all()
    serializer_class = BookReadSerializer
    permission_classes = [IsSuperUserOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ['title']

    def get_serializer_class(self):
        if self.action in ['create']:
            return BookWriteSerializer
        return super().get_serializer_class()
