from django.shortcuts import render
from django.http import HttpResponse
from .models import SerumLevelLog
from .models import Patient
from .models import SerumType

# Create your views here.
def indexPageView(request) :
    data = None
    return render(request, 'personal/index.html')

def foodJournalView(request) :
    return render(request, 'personal/journal.html')

def addFoodView(request) :
    return render(request, 'personal/food.html')

def levelsLogView(request) :
    data = SerumLevelLog.objects.all()
    context = {
        "serum" : data
    }
    return render(request, 'personal/serumlevels.html', context)

def addLevelView(request) :
    if request.method == 'POST':
        
        serum = SerumLevelLog()

        serum.log_date = request.POST['log_date']
        serum.level = request.POST['level']
        serum.serum_type = request.POST['serum_name']

        return levelsLogView(request)
    else:
        data = SerumType.objects.all()
        context = {
            "serum" : data
        }
        return render(request, 'personal/serumform.html', context)

def deleteLogView(request, type, pat) :
    data = SerumLevelLog.objects.get(serum_type = type, patient =pat)
    data.delete()
    return levelsLogView(request)