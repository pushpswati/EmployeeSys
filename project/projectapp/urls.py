from django.conf.urls import url
from projectapp import views
from .views import FileView

urlpatterns=[
url(r'^employeelist$',views.EmployeeList.as_view(),name='EmployeeList'),
url(r'^employeegetdata$',views.EmployeeListGetData.as_view(),name='EmployeeListGetData'),
url(r'^upload/$', FileView.as_view(), name='file-upload'),
]

