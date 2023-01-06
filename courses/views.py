from django.shortcuts import render
from rest_framework import viewsets
from courses.serializers import CourseSerializer
from courses.models import Course

# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
