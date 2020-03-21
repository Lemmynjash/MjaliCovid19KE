from django.shortcuts import render
from django.http import HttpResponse
from .models import Case
from datetime import date
from victims.models import Victims


# Create your views here.
def dashboard(request):
    
    confirmedcases =Case.objects.count()
    
    hospitalizedcases=Case.objects.filter(status='In Hospital').count()
    mycases =Case.objects
    
    if confirmedcases!=0 and hospitalizedcases!=0:
        results=confirmedcases/hospitalizedcases
    else:
        results=0    
        
    totalPercentage=(results * 100)
    
    intensivecare=Case.objects.filter(status='Intensive Care').count()
    
    recoveredpatients=Case.objects.filter(status='Recovered').count()
    
    today = date.today()
    dateToday=today.strftime("%B %d, %Y")
    
    male=Victims.objects.filter(gender='Male').count()
    female=Victims.objects.filter(gender='Female').count()

    kenyan=Victims.objects.filter(citizen='Kenyan').count()
    spanish=Victims.objects.filter(citizen='Spanish').count()
    burundians=Victims.objects.filter(citizen='Burundian').count()
    
    localTransmission=Case.objects.filter(infection_source='Local Transmission').count()
    importedCase=Case.objects.filter(infection_source='Imported Cases').count()
    
    totalSource=(localTransmission+importedCase)
    
    if totalSource!=0:
        localResults=localTransmission/totalSource
        importedResult=importedCase/totalSource
    else:
        localResults=0    
        importedResult=0
        
        
    totalLocalPercentage=(localResults * 100)
    totalImportedPercentage=(importedResult * 100)
    
    placesoforigins=Country.objects.all()
    
    allclusters
    print(dateToday)
    print(str(confirmedcases)+' my cases')
    print(str(mycases)+' all cases')
    print(str(hospitalizedcases)+' all cases in hospital')
    print(str(totalPercentage)+' 100% all cases in hospital')
    
    return render(request,"dashboard.html",{'confirmedcases':confirmedcases,
                                            'mycases':mycases,
                                             'hospitalizedcases':hospitalizedcases,
                                             'totalPercentage':totalPercentage,
                                             'intensivecare':intensivecare,
                                             'recoveredpatients':recoveredpatients,
                                             'dateToday':dateToday,
                                             'male':male,
                                             'female':female,
                                             'kenyan':kenyan,
                                             'spanish':spanish,
                                             'burundians':burundians,
                                             'localTransmission':localTransmission,
                                             'importedCase':importedCase,
                                             'totalLocalPercentage':totalLocalPercentage,
                                             'totalImportedPercentage':totalImportedPercentage})