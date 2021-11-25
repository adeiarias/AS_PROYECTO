from django.urls import path, include
from .views import MessageSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('messages', MessageSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]