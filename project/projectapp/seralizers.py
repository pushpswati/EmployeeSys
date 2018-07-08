from rest_framework import serializers
from projectapp.models import Employee
from .models import File


class EmployeeSerializer(serializers.ModelSerializer):
class FileSerializer(serializers.ModelSerializer):


    class Meta:

        model=Employee
        fields=('created','employeename','employeesalary')
        model = File
        fields = ('file', 'remark', 'timestamp')
        
       
