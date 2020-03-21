from django.shortcuts import render

# Create your views here.
def currentcase(request):
    return render(request,'currentcase.html')