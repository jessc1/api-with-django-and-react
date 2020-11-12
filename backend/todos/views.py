from django.shortcuts import render
from rest_framework import generics
from .models import Todos
from .serializers import TodoSerializer


# Create your views here.
class ListTodo(generics.ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

