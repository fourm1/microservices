from django.shortcuts import render
from rest_framework import viewsets

from school_app.models import School
from school_app.serializers import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer