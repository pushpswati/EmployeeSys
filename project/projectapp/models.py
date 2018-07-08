from django.db import models

class Employee(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      employeename = models.CharField(max_length=100, blank=True,default='')
      employeesalary = models.IntegerField()


class File(models.Model):
      file = models.FileField(blank=False, null=False)
      remark = models.CharField(max_length=20)
      timestamp = models.DateTimeField(auto_now_add=True)
    
      class Meta:
           ordering = ('created',)
