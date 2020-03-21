from django.shortcuts import render

# Create your views here.
def symptomatic(request):
    return render(request,'symptomatic.html')