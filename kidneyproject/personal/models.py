from django.db import models

# Create your models here.
class Comorbidity(models.Model) :
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)

    def __str__(self) :
        return (self.name)

class KidneyStage(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self) :
        return (self.name)
class Patient(models.Model) :
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.BigIntegerField()
    weight = models.DecimalField(max_digits=3, decimal_places=2)
    height = models.BigIntegerField()
    kidney_stage = models.ForeignKey(KidneyStage, on_delete=models.DO_NOTHING)
    comorbidity = models.ManyToManyField(Comorbidity, blank=True)
    unit_preference = models.CharField(max_length=20)

    def __str__(self) :
        return (self.first_name + ' ' + self.last_name)

class MealLog(models.Model) :
    log_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    meal_type = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)

    def __str__(self) :
        return (self.log_date + ' ' + self.meal_type)

class Food(models.Model) :
    measurement_type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    calories_kJ = models.BigIntegerField()
    water_g = models.DecimalField(max_digits=3, decimal_places=1)
    protein_g = models.DecimalField(max_digits=3, decimal_places=1)
    total_fat_g = models.DecimalField(max_digits=3, decimal_places=1)
    total_fiber_g = models.DecimalField(max_digits=3, decimal_places=1)
    alcohol_g = models.DecimalField(max_digits=3, decimal_places=1)
    total_sugars_g = models.DecimalField(max_digits=3, decimal_places=1)
    added_sugars_g = models.DecimalField(max_digits=3, decimal_places=1)
    total_carbs_g = models.DecimalField(max_digits=3, decimal_places=1)
    ca_g = models.DecimalField(max_digits=3, decimal_places=1)
    phos_g = models.DecimalField(max_digits=3, decimal_places=1)
    k_g = models.DecimalField(max_digits=3, decimal_places=1)
    na_g = models.DecimalField(max_digits=3, decimal_places=1)
    total_saturated_fat_g = models.DecimalField(max_digits=3, decimal_places=1)
    total_unsaturated_fat_g = models.DecimalField(max_digits=3, decimal_places=1)
    
    def __str__(self) :
        return (self.name)

class FoodinMeal(models.Model) :
    amount = models.BigIntegerField()
    meal_log = models.ForeignKey(MealLog, on_delete=models.DO_NOTHING)
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)

    def __str__(self) :
        return (self.food)

class SerumType(models.Model) :
    name = models.CharField(max_length=50)
    units = models.CharField(max_length=50)

    def __str__(self) :
        return (self.name)

class SerumLevelLog(models.Model) :
    log_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    level = models.DecimalField(max_digits=6, decimal_places=2)
    serum_type = models.ForeignKey(SerumType, on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)

    def __str__(self) :
        return (self.log_date)