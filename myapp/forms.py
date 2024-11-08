from django import forms

class EmployeeForm(forms.Form):
    
    name = forms.CharField(max_length=100, required=False)
    
    contact = forms.CharField(max_length=15, required=False)
    
    salary = forms.IntegerField(required=False)
    
    designation = forms.CharField(max_length=100, required=False)
    
    department = forms.CharField(max_length=100, required=False)
    
    def clean_salary(self):
        
        salary = self.cleaned_data.get('salary')
        
        if salary < 50000 or salary > 100000:
            
            errmsg = "Salary must be between 50,000 and 100,000"
            
            self.add_error("salary", errmsg)
            
        else:
            
            return salary
