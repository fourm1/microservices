from django.shortcuts import render
from rest_framework import viewsets, status

from student_app.consul_client import discover_service
from student_app.models import Student
from student_app.serializers import StudentSerializer

from rest_framework.response import Response
import requests


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def retrieve(self, request, pk=None):
        queryset = Student.objects.get(pk=pk)
        serializer = self.get_serializer(queryset, many=False)
        r = requests.get(f'http://0.0.0.0:8002/schools/{queryset.school_id}')
        school = r.json()
        return Response({'id': serializer.data['id'], 'name': serializer.data['name'], 'genre': serializer.data['genre'], 'school': school}, status=status.HTTP_200_OK)
