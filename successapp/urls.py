from django.urls import path
from .views import CommentSerialze
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'comments', CommentSerialze, basename='CommentSerialze')

urlpatterns = [
    path('', include(router.urls)),
]






