from django.shortcuts import render

# Create your views here.

def confirmed(request):
    return render(request,'confirmed.html')