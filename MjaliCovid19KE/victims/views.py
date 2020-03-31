from django.shortcuts import redirect, render
from .forms import AddNewVictims

def victims(request):
    return render(request,'victims.html')

def addvictims(request):

    if request.method=='POST':
        form=AddNewVictims(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('addvictims')
        else:
            return render(request,'addvictims.html',{'form':form})

    elif request.method=="GET":
        form=AddNewVictims() 
        return render(request, 'addvictims.html', {'form':form})
    
