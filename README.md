# EmployeeSys
employee salary system

## Ubuntu 16.04

#EmployeeSys API:

## API Signature:-
Step1: All Employee list 
api:-     
http://0.0.0.0:8002/employeelist

Step2: Get Employee hightest salary
api:-
http://0.0.0.0:8002/employeegetdata

step3: upload file
api:-
http://0.0.0.0:8002/upload


#Setup Installation

## Run Following Command

sudo apt-get update
sudo apt-get install python

### Python inbuild runserver command

python manage.py runserver

### for updating a table

python manage.py makemigrations

### for creating a database

python manage.py migrate





