from django.shortcuts import render
from rest_framework import viewsets

from .models import Data
from .serializers import MessageSerializer


class MessageSet(viewsets.ModelViewSet):
    queryset  = Data.objects.all()
    serializer_class = MessageSerializer
