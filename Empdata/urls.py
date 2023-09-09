from django.urls import path, include
from . import views

urlpatterns = [
    path('add_employee/', views.add_employee, name='add_employee'),
    # path('api/employee/', views.EmployeeList.as_view(), name='employee-list'),
    # path('api/', views.EmployeeList.as_view()), 
   
    path('add_employee/', views.add_employee, name='add_employee'),
    path('send_birthday_wishes/', views.send_birthday_wishes, name='send_birthday_wishes'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_detail/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('delete_record/<int:employee_id>/', views.delete_employee, name='delete_record' ),
    path('birthday_check/', views.birthday_check, name='birthday_check'),
    path('send_birthday_wishes/', views.send_birthday_wishes, name='send_birthday_wishes'),
]    



