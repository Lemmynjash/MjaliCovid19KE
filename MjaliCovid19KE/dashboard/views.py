from django.shortcuts import render
from django.http import HttpResponse
from .models import Case
from datetime import date
from .models import Victims
from .models import Country
import datetime

# Create your views here.


def dashboard(request):

    confirmedcases = Case.objects.count()
    totalVictims = Victims.objects.count()

    hospitalizedcases = Case.objects.filter(status=1).count()
    mycases = Case.objects.all().order_by('-id')[:5]

    if confirmedcases != 0 and hospitalizedcases != 0:
        results = confirmedcases/hospitalizedcases
    else:
        results = 0

    totalPercentage = (results * 100)

    intensivecare = Case.objects.filter(status=4).count()

    recoveredpatients = Case.objects.filter(status=2).count()

    today = date.today()
    dateToday = today.strftime("%B %d, %Y")

    male = Victims.objects.filter(gender='Male').count()
    female = Victims.objects.filter(gender='Female').count()

    kenyan = Victims.objects.filter(citizen='Kenyan').count()
    spanish = Victims.objects.filter(citizen='Spanish').count()
    burundians = Victims.objects.filter(citizen='Burundian').count()
    french = Victims.objects.filter(citizen='French').count()
    mexicans = Victims.objects.filter(citizen='Mexican').count()
    foreigners = Victims.objects.filter(citizen='Foreigner').count()

    if totalVictims != 0:
        malePercentage = (male/totalVictims)*100
        femalePercentage = (female/totalVictims)*100
        kenyanPercentage = (kenyan/totalVictims)*100
        spanishPercentage = (spanish/totalVictims)*100
        burundiansPercentage = (burundians/totalVictims)*100
        frenchPercentage = (french/totalVictims)*100
        mexicansPercentage = (mexicans/totalVictims)*100
        foreignersPercentage = (foreigners/totalVictims)*100
    else:
        malePercentage = 0
        femalePercentage = 0
        kenyanPercentage = 0
        spanishPercentage = 0
        burundiansPercentage = 0
        frenchPercentage = 0
        mexicansPercentage = 0
        foreignersPercentage = 0

    localTransmission = Case.objects.filter(infection_source=2).count()
    importedCase = Case.objects.filter(infection_source=1).count()

    totalSource = (localTransmission+importedCase)

    if totalSource != 0:
        localResults = localTransmission/totalSource
        importedResult = importedCase/totalSource
    else:
        localResults = 0
        importedResult = 0

    totalLocalPercentage = (localResults * 100)
    totalImportedPercentage = (importedResult * 100)

    placesoforigins = Country.objects.all()

    myLastCase = Case.objects.order_by('-id')[0]

    print(myLastCase.confirmed_date)

    start = datetime.date(2020, 3, 12)
    #end = datetime.date(myLastCase.confirmed_date.timetuple()[:3])
    end = datetime.date(2020,4,7)#thi one i will have to do a major research
    dateList = date_range(start, end)

    syptomaticAt=[]
    confirmedAt=[]
    recoveredAt=[]
    for dt in dateList:
        print(dt.strftime("%Y-%m-%d"))
        confimedCount = Case.objects.filter(confirmed_date=dt.strftime("%Y-%m-%d")).count()
        symptomaticAtCount = Case.objects.filter(symptopmatic_at=dt.strftime("%Y-%m-%d")).count()
        recoveredCount = Case.objects.filter(recovered_at=dt.strftime("%Y-%m-%d")).count()
        
        syptomaticAt.append(symptomaticAtCount)
        confirmedAt.append(confimedCount)
        recoveredAt.append(recoveredCount)
    
    print(dateToday)
    print(str(hospitalizedcases)+' all cases in hospital')
    print(str(totalPercentage)+' 100% all cases in hospital')

    myContext = {'confirmedcases': confirmedcases,
                 'mycases': mycases,
                 'hospitalizedcases': hospitalizedcases,
                 'totalPercentage': round(totalPercentage, 1),
                 'intensivecare': intensivecare,
                 'recoveredpatients': recoveredpatients,
                 'dateToday': dateToday,
                 'male': male,
                 'female': female,
                 'kenyan': kenyan,
                 'spanish': spanish,
                 'burundians': burundians,
                 'localTransmission': localTransmission,
                 'importedCase': importedCase,
                 'totalLocalPercentage': round(totalLocalPercentage, 1),
                 'totalImportedPercentage': round(totalImportedPercentage, 1),
                 'malePercentage': round(malePercentage, 1),
                 'femalePercentage': round(femalePercentage, 1),
                 'kenyanPercentage': round(kenyanPercentage, 1),
                 'spanishPercentage': round(spanishPercentage, 1),
                 'burundiansPercentage': round(burundiansPercentage, 1),
                 'frenchPercentage': round(frenchPercentage, 1),
                 'mexicansPercentage': round(mexicansPercentage, 1),
                 'foreignersPercentage': round(foreignersPercentage, 1),
                 'french': french,
                 'mexicans': mexicans,
                 'foreigners': foreigners,
                 'dateList':dateList,
                 
                 }

    return render(request, "dashboard.html", myContext)


def date_range(start, end):
    r = (end+datetime.timedelta(days=1)-start).days
    return [start+datetime.timedelta(days=i) for i in range(r)]

