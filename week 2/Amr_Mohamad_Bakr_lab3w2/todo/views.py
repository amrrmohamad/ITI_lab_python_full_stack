from django.shortcuts import render
from rest_framework import viewsets
from .models import ToDo
from .serializers import ToDoSerializer

# Create your views here.

class ToDoViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD operations on To-Do items.
    """
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
