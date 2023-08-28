from django.contrib import admin
from django.urls import path, include
from assets.views import CompanyList, EmployeeList, DeviceList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies/', CompanyList.as_view(), name='company-list'),
    path('api/employees/', EmployeeList.as_view(), name='employee-list'),
    path('api/devices/', DeviceList.as_view(), name='device-list'),
]
