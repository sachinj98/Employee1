from django.urls import path, include
from Empdata.api.views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('api/Emplist/',views.ListEmployeeAPIView.as_view(), basename="employee_list")
# router.register('api/createemp/', views.CreateEmployeeAPIView.as_view(), basename="emp_create" )
# router.register('api/updateemp/', views.UpdateEmployeeAPIView.as_view(), basename="update_emp" )
# router.register('api/delete/', views.DeleteEmployeeAPIView.as_view(), basename="delete_emp")


router.register(r'employees', EmployeeViewSet)
urlpatterns = [
    path('', include(router.urls))
]
