from snippets.models import *
from snippets.serializers import *
from rest_framework import generics, viewsets
from django.shortcuts import render

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CategoriesView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
	
