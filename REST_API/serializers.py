from rest_framework import serializers
from .models import Employeedetail


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeedetail
        fields = '__all__'
