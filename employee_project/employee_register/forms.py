from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        #fields = '__all__'  #this means all field in class employee are used
        #fields = ('fullname', 'emp_code', 'mobile','position')
        fields = ('fullname', 'emp_code', 'mobile','position')  #use this if only few fields in the class is needed, even rearrange it
        labels = {
            'fullname': 'Full Name',
            'emp_code' : 'EMP. Code'
        }

    def __init__(self, *args, **kwargs):        #this entire function is to have a display in the drop down instead of ----------
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select Position"
        self.fields['emp_code'].required = False   #do this if a text field or any field does necessary need an