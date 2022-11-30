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
    patient_id = str(data.id)
    current_date = str(date.today())
    context = {
        "pat" : data,
        "calories_kj" : 0,
        "water_g" : 0,
        "protein_g" : 0,
        "total_fat_g" : 0,
        "total_fiber_g" : 0,
        "alcohol_g" : 0,
        "total_sugars_g" : 0,
        "added_sugars_g" : 0,
        "total_carbs_g" : 0,
        "ca_mg" : 0,
        "phos_mg" : 0,
        "k_mg" : 0,
        "na_mg" : 0,
        "total_saturated_fat_g" : 0,
        "total_unsaturated_fat_g" : 0,
        "RDA_water": 3200,
        "RDA_protein": 0.8,
        "RDA_na": 2300,
        "RDA_carbs": 300
    }
    foods =[]
    for p in Patient.objects.raw("SELECT pp.id, amount, calories_kj, water_g, protein_g, total_fat_g, total_fiber_g, alcohol_g, total_sugars_g, added_sugars_g, total_carbs_g, ca_mg, phos_mg, k_mg, na_mg, total_saturated_fat_g, total_unsaturated_fat_g FROM personal_patient pp INNER JOIN personal_meallog ml ON pp.id = ml.patient_id INNER JOIN personal_foodinmeal fm ON ml.id = fm.meal_log_id INNER JOIN personal_food f ON fm.food_id = f.id WHERE pp.id =" + patient_id + " AND log_date = '" + current_date + "'") :
        foods.append(p)

    for food in foods :
        if data.unit_preference == "us" :
            gram_amount = food.amount * 28.35
        else :
            gram_amount = food.amount
        per_value = gram_amount / 100
        final_value = per_value * food.calories_kj
        context["calories_kj"] += final_value
        final_value = per_value * float(food.water_g)
        context["water_g"] += final_value
        final_value = per_value * float(food.protein_g)
        context["protein_g"] += final_value
        final_value = per_value * float(food.total_fat_g)
        context["total_fat_g"] += final_value
        final_value = per_value * float(food.total_fiber_g)
        context["total_fiber_g"] += final_value
        final_value = per_value * float(food.alcohol_g)
        context["alcohol_g"] += final_value
        final_value = per_value * float(food.total_sugars_g)
        context["total_sugars_g"] += final_value
        final_value = per_value * float(food.added_sugars_g)
        context["added_sugars_g"] += final_value
        final_value = per_value * float(food.total_carbs_g)
        context["total_carbs_g"] += final_value
        final_value = per_value * float(food.ca_mg)
        context["ca_mg"] += final_value
        final_value = per_value * float(food.phos_mg)
        context["phos_mg"] += final_value
        final_value = per_value * float(food.k_mg)
        context["k_mg"] += final_value
        final_value = per_value * float(food.na_mg)
        context["na_mg"] += final_value
        final_value = per_value * float(food.total_saturated_fat_g)
        context["total_saturated_fat_g"] += final_value
        final_value = per_value * float(food.total_unsaturated_fat_g)
        context["total_unsaturated_fat_g"] += final_value

    return render(request, 'personal/index.html', context)

def foodJournalView(request, userid, date1) :
    data = Patient.objects.get(id=userid)
    if date1 == 'today' :
        date1 = str(date.today())
    elif date1 == 'other' :
        date1 = request.POST['sDate']
        date1 = str(date1)

    breakfast = []
    lunch = []
    dinner = []
    snacks = []
    for p in FoodinMeal.objects.raw("SELECT * FROM personal_foodinmeal fm INNER JOIN personal_meallog ml ON fm.meal_log_id = ml.id WHERE ml.meal_type = 'breakfast' AND patient_id=" + str(userid) + " AND ml.log_date='" + str(date1) + "'"):
        breakfast.append(p)
    for p in FoodinMeal.objects.raw("SELECT * FROM personal_foodinmeal fm INNER JOIN personal_meallog ml ON fm.meal_log_id = ml.id WHERE ml.meal_type = 'lunch' AND patient_id=" + str(userid) + " AND ml.log_date='" + str(date1) + "'"):
        lunch.append(p)
    for p in FoodinMeal.objects.raw("SELECT * FROM personal_foodinmeal fm INNER JOIN personal_meallog ml ON fm.meal_log_id = ml.id WHERE ml.meal_type = 'dinner' AND patient_id=" + str(userid) + " AND ml.log_date='" + str(date1) + "'"):
        dinner.append(p)
    for p in FoodinMeal.objects.raw("SELECT * FROM personal_foodinmeal fm INNER JOIN personal_meallog ml ON fm.meal_log_id = ml.id WHERE ml.meal_type = 'snacks' AND patient_id=" + str(userid) + " AND ml.log_date='" + str(date1) + "'"):
        snacks.append(p)

    context = {
        "pat" : data,
        "breakfast" : breakfast,
        "lunch" : lunch,
        "dinner" : dinner,
        "snacks" : snacks,
        "showDate" : date1,
        "calories_kj" : 0,
        "water_g" : 0,
        "protein_g" : 0,
        "total_fat_g" : 0,
        "total_fiber_g" : 0,
        "alcohol_g" : 0,
        "total_sugars_g" : 0,
        "added_sugars_g" : 0,
        "total_carbs_g" : 0,
        "ca_mg" : 0,
        "phos_mg" : 0,
        "k_mg" : 0,
        "na_mg" : 0,
        "total_saturated_fat_g" : 0,
        "total_unsaturated_fat_g" : 0
    }
    #Calculate food nutrients
    foods =[]
    for p in Patient.objects.raw("SELECT pp.id, amount, calories_kj, water_g, protein_g, total_fat_g, total_fiber_g, alcohol_g, total_sugars_g, added_sugars_g, total_carbs_g, ca_mg, phos_mg, k_mg, na_mg, total_saturated_fat_g, total_unsaturated_fat_g FROM personal_patient pp INNER JOIN personal_meallog ml ON pp.id = ml.patient_id INNER JOIN personal_foodinmeal fm ON ml.id = fm.meal_log_id INNER JOIN personal_food f ON fm.food_id = f.id WHERE pp.id =" + str(userid) + " AND log_date = '" + date1 + "'") :
        foods.append(p)

    for food in foods :
        if data.unit_preference == "us" :
            gram_amount = food.amount * 28.35
        else :
            gram_amount = food.amount
        per_value = gram_amount / 100
        final_value = per_value * food.calories_kj
        context["calories_kj"] += final_value
        final_value = per_value * float(food.water_g)
        context["water_g"] += final_value
        final_value = per_value * float(food.protein_g)
        context["protein_g"] += final_value
        final_value = per_value * float(food.total_fat_g)
        context["total_fat_g"] += final_value
        final_value = per_value * float(food.total_fiber_g)
        context["total_fiber_g"] += final_value
        final_value = per_value * float(food.alcohol_g)
        context["alcohol_g"] += final_value
        final_value = per_value * float(food.total_sugars_g)
        context["total_sugars_g"] += final_value
        final_value = per_value * float(food.added_sugars_g)
        context["added_sugars_g"] += final_value
        final_value = per_value * float(food.total_carbs_g)
        context["total_carbs_g"] += final_value
        final_value = per_value * float(food.ca_mg)
        context["ca_mg"] += final_value
        final_value = per_value * float(food.phos_mg)
        context["phos_mg"] += final_value
        final_value = per_value * float(food.k_mg)
        context["k_mg"] += final_value
        final_value = per_value * float(food.na_mg)
        context["na_mg"] += final_value
        final_value = per_value * float(food.total_saturated_fat_g)
        context["total_saturated_fat_g"] += final_value
        final_value = per_value * float(food.total_unsaturated_fat_g)
        context["total_unsaturated_fat_g"] += final_value

    return render(request, 'personal/journal.html', context)

def addFoodView(request, userid) :
    data = Patient.objects.get(id=userid)
    date1 = str(date.today())
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

        return foodJournalView(request, userid, date1)
    else:
        return render(request, 'personal/food.html', context)

def levelsLogView(request, userid) :
    data = SerumLevelLog.objects.filter(patient=userid)
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

def foodinMealView(request, userid, mealtype, logid, date1) :
    data = Patient.objects.get(id=userid)
    food = Food.objects.all()
    current_date = str(date.today())
    context = {
        "pat" : data,
        "mealtypekey" : mealtype,
        "logidkey" : logid,
        "food" : food,
        "showDate" : date1
    }
    if request.method == 'POST' :
        food_in = FoodinMeal()

        meallog1 = request.POST['logid']
        food_in.meal_log = MealLog.objects.get(id=meallog1)      
        food_in.amount = request.POST['amount']
        foodid = request.POST['food']
        food_in.food = Food.objects.get(id=foodid)

        food_in.save()

        return foodJournalView(request, userid, date1)
    else :
        if logid == 0:
            current_log = []
            user_string = str(userid)
            for p in MealLog.objects.raw("SELECT * FROM personal_meallog WHERE meal_type='" + mealtype + "' AND patient_id=" + user_string + " AND log_date='" + date1 + "'") :
                current_log.append(p)
            if len(current_log) > 0 :
                meal_log_id = current_log[0].id

                return foodinMealView(request, userid, mealtype, meal_log_id, date1)
            else :
                meallog2 = MealLog()

                meallog2.log_date = str(date1)
                meallog2.meal_type = mealtype
                meallog2.patient = Patient.objects.get(id=userid)
                meallog2.save()

                meal_log_id = meallog2.id

                return foodinMealView(request, userid, mealtype, meal_log_id, date1)
        else :
            return render(request, 'personal/foodinmeal.html', context)

