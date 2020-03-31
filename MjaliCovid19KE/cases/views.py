from django.shortcuts import redirect, render
from dashboard.models import Victims
from dashboard.models import Case
from dashboard.models import Country
from .forms import AddNewCaseForm

# Create your views here.

def cases(request):
    return render(request,'cases.html')

def addnewcase(request):
    
    if request.method=='POST':
        form=AddNewCaseForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('addnewcase')
        else:
            return render(request,'newcases.html',{'form':form})
        
    elif request.method=="GET":
        form=AddNewCaseForm() 
        return render(request, 'newcases.html', {'form':form})