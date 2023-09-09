
from rest_framework import generics
from Empdata.models import *
from .serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import viewsets

# class EmployeeListView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class ListEmployeeAPIView(ListAPIView):
#     """Lists all Employees from the database"""
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class CreateEmployeeAPIView(CreateAPIView):
#     """Creates a new Employee"""
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class UpdateEmployeeAPIView(UpdateAPIView):
#     """Update the Employee whose id has been passed through the request"""
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class DeleteEmployeeAPIView(DestroyAPIView):
#     """Deletes a Employee whose id has been passed through the request"""
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer 


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A viewset for CRUD operations on Employee objects.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer