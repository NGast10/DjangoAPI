from django.shortcuts import render
from rest_framework import viewsets
from .models import fizzBuzz
from .serializers import fizzBuzzSerializer
#from rest_framework import generics

#Creates the view for the API will using the model and serializer
class fizzBuzzListView(viewsets.ModelViewSet):
	queryset = fizzBuzz.objects.all()
	serializer_class = fizzBuzzSerializer

