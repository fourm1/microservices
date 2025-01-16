from rest_framework import serializers

from school_app.models import School

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'address', 'directorName']