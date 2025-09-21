from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet


router_api_v1 = DefaultRouter()

router_api_v1.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('', include(router_api_v1.urls)),
]
