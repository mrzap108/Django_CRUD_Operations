from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        #fields = '__all__'  #this means all field in class employee are used
        #fields = ('fullname', 'emp_code', 'mobile','position')
        fields = ('fullname', 'emp_code', 'mobile','position')  #use this if only few fields in the class is needed, even rearrange it
