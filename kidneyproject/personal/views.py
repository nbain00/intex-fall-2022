from django.shortcuts import render
from django.http import HttpResponse
from .models import SerumLevelLog
from .models import Patient
from .models import SerumType
from .models import KidneyStage, Comorbidity
from .models import Food, MealLog, FoodinMeal
from datetime import date


# Create your views here.
def indexPageView(request) :
    data = Patient.objects.get(id=1)

    context = {
        "pat" : data
    }
    return render(request, 'personal/index.html', context)

def foodJournalView(request, userid) :
    data = Patient.objects.get(id=userid)
    '''data2 = MealLog.objects.filter(patient=userid)
    data3 = FoodinMeal.objects.select_related('meal_log')'''
    breakfast = []
    lunch = []
    dinner = []
    snacks = []
    for p in FoodinMeal.objects.raw("SELECT * FROM personal_foodinmeal fm INNER JOIN personal_meallog ml ON fm.meal_log_id = ml.id WHERE ml.meal_type = 'breakfast' AND patient_id=" + str(userid)):
        breakfast.append(p)
    for p in FoodinMeal.objects.raw("SELECT * FROM personal_foodinmeal fm INNER JOIN personal_meallog ml ON fm.meal_log_id = ml.id WHERE ml.meal_type = 'lunch' AND patient_id=" + str(userid)):
        lunch.append(p)
    for p in FoodinMeal.objects.raw("SELECT * FROM personal_foodinmeal fm INNER JOIN personal_meallog ml ON fm.meal_log_id = ml.id WHERE ml.meal_type = 'dinner' AND patient_id=" + str(userid)):
        dinner.append(p)
    for p in FoodinMeal.objects.raw("SELECT * FROM personal_foodinmeal fm INNER JOIN personal_meallog ml ON fm.meal_log_id = ml.id WHERE ml.meal_type = 'snacks' AND patient_id=" + str(userid)):
        snacks.append(p)

#     entry = Entry.objects.select_related('blog').get(id=5)
# or
# entries = Entry.objects.filter(foo='bar').select_related('blog')

    context = {
        "pat" : data,
        "breakfast" : breakfast,
        "lunch" : lunch,
        "dinner" : dinner,
        "snacks" : snacks
    }
    return render(request, 'personal/journal.html', context)

def addFoodView(request, userid) :
    data = Patient.objects.get(id=userid)
    context = {
        "pat" : data
    }
    if request.method == 'POST' :
        food = Food()

        food.measurement_type = request.POST['measurement_type']
        food.name = request.POST['name']
        food.calories_kj = request.POST['calories_kj']
        food.water_g = request.POST['water_g']
        food.protein_g = request.POST['protein_g']
        food.total_fat_g = request.POST['total_fat_g']
        food.total_fiber_g = request.POST['total_fiber_g']
        food.alcohol_g = request.POST['alcohol_g']
        food.total_sugars_g = request.POST['total_sugars_g']
        food.added_sugars_g = request.POST['added_sugars_g']
        food.total_carbs_g = request.POST['total_carbs_g']
        food.ca_g = request.POST['ca_g']
        food.phos_g = request.POST['phos_g']
        food.k_g = request.POST['k_g']
        food.na_g = request.POST['na_g']
        food.total_saturated_fat_g = request.POST['total_saturated_fat_g']
        food.total_unsaturated_fat_g = request.POST['total_unsaturated_fat_g']

        food.save()

        return render(request, 'personal/journal.html', context)
    else:
        return render(request, 'personal/food.html', context)

def levelsLogView(request, userid) :
    data = SerumLevelLog.objects.get(userid)
    data2 = Patient.objects.get(id=userid)
    context = {
        "serum" : data,
        "pat" : data2
    }
    return render(request, 'personal/serumlevels.html', context)

def addLevelView(request, userid) :
    data = Patient.objects.get(id=userid)
    context = {
        "pat" : data
    }
    if request.method == 'POST':
        
        serum = SerumLevelLog()

        serum.log_date = request.POST['log_date']
        serum.level = request.POST['level']
        pat_id = request.POST['pat_id']
        serum.patient = Patient.objects.get(id=pat_id)
        tipe = request.POST['serum_name']
        serum.serum_type = SerumType.objects.get(id=tipe)
        serum.save()
        return levelsLogView(request, pat_id)
    else:
        data2 = SerumType.objects.all()
        context["serum"] = data2

        return render(request, 'personal/serumform.html', context)

def deleteLogView(request, userid, logid,) :
    data = SerumLevelLog.objects.get(id=logid)
    data2 = Patient.objects.get(id=userid)
    pat_id = data2.id
    data.delete()
    return levelsLogView(request, pat_id)
    
def profileEditView(request, userid) :
    data = Patient.objects.get(id=userid)
    data2 = Comorbidity.objects.all()
    data3 = KidneyStage.objects.all()
    context = {
        "pat" : data,
        "profile" : data,
        "comor" : data2,
        "stage" : data3
    }
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

        return render(request, 'personal/index.html', context)

    else:
        return render(request, 'personal/profileview.html', context)

def foodinMealView(request, userid, mealtype, logid) :
    data = Patient.objects.get(id=userid)
    context = {
        "pat" : data
    }
    if request.method == 'POST' :
        return HttpResponse('go cougs')
    else :
        if logid == 0:
            current_log = []
            user_string = str(userid)
            current_date = str(date.today())
            for p in MealLog.objects.raw("SELECT * FROM personal_meallog WHERE meal_type='" + mealtype + "' AND patient_id=" + user_string + " AND log_date='" + current_date + "'") :
                current_log.append(p)
            if len(current_log) > 0 :
                meal_log_id = current_log[0].id

                return foodinMealView(request, userid, mealtype, meal_log_id)
            else :
                return HttpResponse("Here we'll create another record")
        else :
            return render(request, 'personal/foodinmeal.html', context)

