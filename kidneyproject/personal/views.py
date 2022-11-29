from django.shortcuts import render
from django.http import HttpResponse
from .models import SerumLevelLog
from .models import Patient
from .models import SerumType
from .models import KidneyStage, Comorbidity

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
        tipe = request.POST['serum_name']
        serum.serum_type = SerumType.objects.get(id=tipe)
        serum.save()
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
    
def profileEditView(request, userid) :
    if request.method == 'POST':
        cust_id = request.POST['cust_id']
        profile = Patient.objects.get(id=cust_id)

        profile.first_name = request.POST['first_name']
        profile.last_name = request.POST['last_name']
        profile.age = request.POST['age']
        profile.weight = request.POST['weight']
        profile.height = request.POST['height']
        kstage = request.POST['kidney_stage']
        profile.kidney_stage = (KidneyStage.objects.get(id=kstage))
        cmrb = request.POST['comorbidity']
        profile.comorbidity.add(Comorbidity.objects.get(id=cmrb))
        profile.unit_preference = request.POST['unit_preference']
        profile.save()
        return render(request, 'personal/index.html')

    else:
        data = Patient.objects.get(id=userid)
        data2 = Comorbidity.objects.all()
        data3 = KidneyStage.objects.all()
        context = {
            "profile" : data,
            "comor" : data2,
            "stage" : data3
        }
        return render(request, 'personal/profileview.html', context)
