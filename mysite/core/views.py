from django.shortcuts import render
from django.contrib import messages

from .models import Employees

# Create your views here.


def index(request):
    return render(request, "index.html")


def table(request):
    employees = Employees.objects.order_by("full_name")
    return render(request, "table.html", context={"employees": employees})


def employee_of_month(request):
    return render(request, "employee1.html")


def add_employee_page(request):
    if request.method == "POST":
        return add_employee(request)
    return render(request, "add.html")


def add_employee(request):

    fullname = request.POST["full_name"]
    position = request.POST["position"]
    email = request.POST["email"]

    try:
        new_employee = Employees(
            full_name=fullname, position=position, email=email)
        new_employee.save()
        success = True
    except Exception:
        success = False

    if success:
        messages.add_message(
            request, messages.SUCCESS, "Сотрудник успешно занесён в базу данных"
        )
    else:
        messages.add_message(request, messages.ERROR, "Произошла ошибка")

    return render(request, "add.html")
