from django.shortcuts import render
from dashboard.models import Case
from datetime import date, timedelta, datetime
from dashboard.models import Victims
from dashboard.models import Country


# Create your views here.
def currentcase(request):

    confirmedcases = Case.objects.count()
    totalVictims = Victims.objects.count()

    hospitalizedcases = Case.objects.filter(status=1).count()
    intensivecare = Case.objects.filter(status=4).count()

    recoveredpatients = Case.objects.filter(status=2).count()

    theTotalPercentage = (hospitalizedcases/confirmedcases) * 100

    today = date.today()

    myLastCase = Case.objects.order_by('-id')[0]

    lessThree = today - timedelta(days=3)

    lessFour = today-timedelta(days=4)
    lessSeven = today-timedelta(days=7)
    lessEight = today-timedelta(days=8)
    lessFourteen = today-timedelta(days=14)
    lessFifteen = today-timedelta(days=15)
    lessTwenty = today-timedelta(days=21)

    lessThanThreeDays = Case.objects.filter(
        status=1, confirmed_date=lessThree.strftime('%Y-%m-%d %H:%M:%S')).count()
    fromFourToSeven = Case.objects.filter(status=1, confirmed_date__gte=lessSeven.strftime('%Y-%m-%d %H:%M:%S'),
                                          confirmed_date__lte=lessFour.strftime('%Y-%m-%d %H:%M:%S')).count()
    fromEighteToFouteen = Case.objects.filter(status=1, confirmed_date__gte=lessFourteen.strftime('%Y-%m-%d %H:%M:%S'),
                                              confirmed_date__lte=lessEight.strftime('%Y-%m-%d %H:%M:%S')).count()
    fromFifteenTotwentyOne = Case.objects.filter(status=1, confirmed_date__gte=lessTwenty.strftime('%Y-%m-%d %H:%M:%S'),
                                                 confirmed_date__lte=lessFifteen.strftime('%Y-%m-%d %H:%M:%S')).count()
    greaterThanTwentyOne = Case.objects.filter(
        status=1, confirmed_date__gte=lessTwenty.strftime('%Y-%m-%d %H:%M:%S')).count()

    lessThanThreeDaysPercentage = (lessThanThreeDays/hospitalizedcases) * 100
    fromFourToSevenPercentage = (fromFourToSeven/hospitalizedcases) * 100
    fromEighteToFouteenPercentage = (
        fromEighteToFouteen/hospitalizedcases) * 100
    fromFifteenTotwentyOnePercentage = (
        fromFifteenTotwentyOne/hospitalizedcases) * 100
    greaterThanTwentyOnePercentage = (
        greaterThanTwentyOne/hospitalizedcases) * 100

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

    print(today.strftime('%Y-%m-%d %H:%M:%S'))
    print(lessThanThreeDays)
    print(fromFourToSeven)
    print(fromEighteToFouteen)
    print(fromFifteenTotwentyOne)
    print(greaterThanTwentyOne)

    context = {
        'confirmedcases': confirmedcases,
        'hospitalizedcases': hospitalizedcases,
        'intensivecare': intensivecare,
        'recoveredpatients': recoveredpatients,
        'theTotalPercentage': round(theTotalPercentage, 1),
        'lessThanThreeDays': lessThanThreeDays,
        'fromFourToSeven': fromFourToSeven,
        'fromFifteenTotwentyOne': fromFifteenTotwentyOne,
        'greaterThanTwentyOne': greaterThanTwentyOne,
        'fromEighteToFouteen': fromEighteToFouteen,
        'lessThanThreeDaysPercentage': round(lessThanThreeDaysPercentage, 1),
        'fromFourToSevenPercentage': round(fromFourToSevenPercentage, 1),
        'fromEighteToFouteenPercentage': round(fromEighteToFouteenPercentage, 1),
        'fromFifteenTotwentyOnePercentage': round(fromFifteenTotwentyOnePercentage, 1),
        'greaterThanTwentyOnePercentage': round(greaterThanTwentyOnePercentage, 1),
        'male': male,
        'female': female,
        'kenyan': kenyan,
        'spanish': spanish,
        'burundians': burundians,
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
        'localTransmission': localTransmission,
        'importedCase': importedCase

    }

    return render(request, 'currentcase.html', context)
