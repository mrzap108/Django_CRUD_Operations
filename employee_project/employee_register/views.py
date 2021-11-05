from django.shortcuts import render

#i did not add this, mayeb django added this????
from employee_register.forms import EmployeeForm
#
from .forms import EmployeeForm

# Create your views here.

def employee_list(request):
    return render(request, "employee_register/employee_list.html")

def employee_form(request):  
    form = EmployeeForm()       
    return render(request, "employee_register/employee_form.html", {'form':form})

def employee_delete(request):
    return
