from django.shortcuts import render
from rest_framework import viewsets
from .models import fizzBuzz
from .serializers import fizzBuzzSerializer
#from rest_framework import generics


class fizzBuzzListView(viewsets.ModelViewSet):
	queryset = fizzBuzz.objects.all()
	serializer_class = fizzBuzzSerializer
'''
class fizzBuzzDetailView(viewsets.ModelViewSet):
	queryset=fizzBuzz.objects.all()
	serializer_class=fizzBuzzSerializer
'''
# Create your views here.
