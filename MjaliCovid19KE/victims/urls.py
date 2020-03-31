from django.urls import path

from . import views

urlpatterns=[
    
    path('',views.victims, name='victims'),
    path('addvictims/',views.addvictims, name='addvictims'),
]