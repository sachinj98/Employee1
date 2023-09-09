from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Employee
from .forms import EmployeeForm
from datetime import *
from django.shortcuts import render, get_object_or_404
import socket
from django.utils import timezone




def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'emp_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'employee_detail.html', {'employee': employee})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_emp.html', {'form': form})



def delete_employee(request, employee_id):
    
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        # Delete the employee record
        employee.delete()
        return redirect('employee_list')  

    return render(request, 'delete_employee.html', {'employee': employee})


def birthday_check(request):
    today = date.today()
    employees = Employee.objects.filter(birth_date__month=today.month, birth_date__day=today.day)

    for employee in employees:
        print(f"Today is {employee.name}'s birthday!")

    return render(request, 'birthday_check.html', context = {'employees': employees})



# creating sending birthday wishes function which helps to send email who has birthday today by using django server 
def send_birthday_wishes(request):
    today = date.today()
    employees = Employee.objects.filter(birth_date__month=today.month, birth_date__day=today.day)

    for employee in employees:
        subject = 'Happy Birthday!'
        message = f"Dear {employee.name},\n\nHappy Birthday!\n\nBest wishes,\nYour Company"
        from_email = 'sessionpractice6@gmail.com'
        recipient_list = [employee.email]

        send_mail(subject, message, from_email, recipient_list)

    return render(request, 'birthday_wishes_sent.html',  context = {'employees': employees})



