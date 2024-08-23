from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from employees.models import *
from employees.serializers import *

# Create your views here.
def home(request):
    return render(request, 'home.html', {'message': 'Welcome to the HRMS!'})

@api_view(['POST'])
def add_employee(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

@api_view(['POST'])
def mark_attendance(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        date = request.data.get('date')
        status = request.data.get('status')
        employee.attendance[date] = status
        employee.save()
        return Response({'message': 'Attendance marked successfully'})
    
@api_view(['GET'])
def get_attendance(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return Response(employee.attendance)