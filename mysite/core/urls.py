from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("employees/", views.table),
    path("employees/employee_of_month", views.employee_of_month),
    path("employees/add", views.add_employee_page),
]
