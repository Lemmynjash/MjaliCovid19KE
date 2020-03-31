from django.urls import path

from . import views

urlpatterns=[
    
    path('',views.cases, name='cases'),
    path('addnewcase/',views.addnewcase, name='addnewcase') 
]