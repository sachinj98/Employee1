"""Employee1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Empdata import views
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from Empdata.urls import urlpatterns
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Employee API')



# urlpatterns = [
#     path("",views.ListEmployeeAPIView.as_view(),name="employee_list"),
#     path("create/", views.CreateEmployeeAPIView.as_view(),name="emp_create"),
#     path("update/<int:pk>/",views.UpdateEmployeeAPIView.as_view(),name="update_emp"),
#     path("delete/<int:pk>/",views.DeleteEmployeeAPIView.as_view(),name="delete_emp")
# ]


schema_view = get_schema_view(
    openapi.Info(
        title="Employee API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Empdata.urls")),
    path('employee/', views.employee_list, name = "employee_list1"),
    path('api/', include("Empdata.api.urls")),
    path('api/docs/', include_docs_urls(title="Employee API")),
    path('redoc/', schema_view.with_ui('redoc'), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] 