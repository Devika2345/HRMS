from django.urls import path
from employees.views import *

urlpatterns = [
    path('add-employee/', add_employee, name='add_employee'),
    path('employees/', get_employees, name='get_employees'),
    path('employees/<int:pk>/attendance/', mark_attendance, name='mark_attendance'),
    path('employees/<int:pk>/attendance/details/', get_attendance, name='get_attendance'),
]