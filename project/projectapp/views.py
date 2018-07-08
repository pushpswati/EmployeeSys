from projectapp.models import  Employee
from projectapp.seralizers import EmployeeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .serializers import FileSerializer
from rest_framework.parsers import MultiPartParser, FormParser

from django.http import HttpResponseRedirect






class EmployeeList(APIView):

       def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeListGetData(APIView):
       def get(self, request, format=None):
            
                  #emp_data=Employee.objects.filter(employeename='suresh')
                emp_datas=Employee.objects.filter(created__year='2018', created__month='07')
                  #emp_data=Employee.objects.all().aggregate(Max('employeesalary'))
                  #{'price__max':52000}
                emp_data=Employee.objects.all().order_by("-employeesalary")[1]
                #emp_data=Employee.objects.all().order_by("-employeesalary")
                print("object type: ",type(emp_data))

                for i in emp_datas:
                    print(i.employeesalary,i.employeename)

                #serilizers_data=EmployeeSerializer(emp_data,many=True)

               # for j in emp_data[0]:
                #data={"name":j.employeename,"salary":j.employeesalary}
                
                data={"name":emp_data.employeename,"salary":emp_data.employeesalary}
                return Response(data)

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)           







           
                
            
            
