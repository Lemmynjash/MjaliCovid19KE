from django.shortcuts import render
from dashboard.models import Case
from datetime import date
from dashboard.models import Victims
from dashboard.models import Country
from datetime import datetime

def confirmed(request):
    
    
    confirmedcases = Case.objects.count()
    totalVictims = Victims.objects.count()

    hospitalizedcases = Case.objects.filter(status=1).count()
    intensivecare = Case.objects.filter(status=4).count()

    recoveredpatients = Case.objects.filter(status=2).count()

    start = datetime.date(2020, 3, 12)
    end = datetime.date(2020,4,7)#thi one i will have to do a major research
    dateList = date_range(start, end)
    
    context={'confirmedcases':confirmedcases,
             'hospitalizedcases':hospitalizedcases,
             'intensivecare':intensivecare,
             'recoveredpatients':recoveredpatients
    }
    
    return render(request,'confirmed.html',context)


def date_range(start, end):
    r = (end+datetime.timedelta(days=1)-start).days
    return [start+datetime.timedelta(days=i) for i in range(r)]