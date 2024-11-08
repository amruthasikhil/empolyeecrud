from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import EmployeeForm
from myapp.models import Employee
from django.contrib import messages

#================================= Employee creating ========================================


class EmployeeCreateView(View):
    
    def get(self, request,*args,**kwargs):
        
        print("======================================================")
        
        form_instance=EmployeeForm()
        
        return render(request, 'employee_add.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance=EmployeeForm(request.POST)
        
        print("================================================================")
        
        if form_instance.is_valid():
            
            mydata=form_instance.cleaned_data
            
            print(mydata)
            
            Employee.objects.create(
                
                name=mydata.get("name"),
                
                contact=mydata.get("contact"),
                
                salary=mydata.get("salary"),
                
                designation=mydata.get("designation"),
                
                department=mydata.get("department")
            )
            
            messages.success(request,"Employees added successfully")
            
            return redirect("employee-list")
        
        else:
            data={"form":form_instance}
            
            return render(request, 'employee_add.html',{"form":form_instance})
        
class EmployeeListView(View):
    
    def get(self, request,*args,**kwargs):
        
        form_instance=EmployeeForm()
        
        qs=Employee.objects.all()
        
        
       
        return render(request, 'employee_view.html',{"employees":qs})
    
    
class EmployeeDeleteView(View):
    
    def get(self, request,*args,**kwargs):
        
        print("============================================================================")
         
        id=kwargs.get("pk")
        
        Employee.objects.get(id=id).delete()
       
        return redirect("employee-list")
    
    
class EmployeeDetailsView(View):
    
    def get(self, request,*args,**kwargs):
        
        
        id=kwargs.get("pk")
                
        qs=Employee.objects.get(id=id)
        
        data={
            "name":qs.name,
            
            "contact":qs.contact,
            
            "salary":qs.salary,
            
            "designation":qs.designation,
            
            "department":qs.department
            
        }
       
        form_instance=EmployeeForm(initial=data)
       
        return render(request, 'employee_view_more.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance=EmployeeForm(request.POST)
        
        id=kwargs.get("pk")
        
        if form_instance.is_valid():
            
            my_data=form_instance.cleaned_data
            
            Employee.objects.filter(id=id).update(**my_data)
            
            messages.success(request,"Details updated successfully")

            return redirect("employee-list")
        else:
            
            return render(request, 'employee_view_more.html',{"form":form_instance})