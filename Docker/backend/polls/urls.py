from django.urls import path, include
from .views import MessageSet
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('messages', MessageSet, basename='messages')

urlpatterns = [
    path('', views.home, name='home'),
    path('manage', include(router.urls)),
]