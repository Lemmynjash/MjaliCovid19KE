from django.shortcuts import render

# Create your views here.
def recovered(request):
    return render(request,'recovered.html')