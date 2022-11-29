# Generated by Django 4.1.2 on 2022-11-29 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comorbidity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_type', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=111)),
                ('calories_kJ', models.BigIntegerField()),
                ('water_g', models.DecimalField(decimal_places=1, max_digits=5)),
                ('protein_g', models.DecimalField(decimal_places=1, max_digits=4)),
                ('total_fat_g', models.DecimalField(decimal_places=1, max_digits=5)),
                ('total_fiber_g', models.DecimalField(decimal_places=1, max_digits=4)),
                ('alcohol_g', models.DecimalField(decimal_places=1, max_digits=4)),
                ('total_sugars_g', models.DecimalField(decimal_places=1, max_digits=5)),
                ('added_sugars_g', models.DecimalField(decimal_places=1, max_digits=5)),
                ('total_carbs_g', models.DecimalField(decimal_places=1, max_digits=5)),
                ('ca_g', models.DecimalField(decimal_places=1, max_digits=4)),
                ('phos_g', models.DecimalField(decimal_places=1, max_digits=4)),
                ('k_g', models.DecimalField(decimal_places=1, max_digits=4)),
                ('na_g', models.DecimalField(decimal_places=1, max_digits=4)),
                ('total_saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_unsaturated_fat_g', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='KidneyStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.BigIntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.BigIntegerField()),
                ('unit_preference', models.CharField(max_length=20)),
                ('comorbidity', models.ManyToManyField(blank=True, to='personal.comorbidity')),
                ('kidney_stage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal.kidneystage')),
            ],
        ),
        migrations.CreateModel(
            name='SerumType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('units', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SerumLevelLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateTimeField()),
                ('level', models.DecimalField(decimal_places=2, max_digits=8)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal.patient')),
                ('serum_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal.serumtype')),
            ],
        ),
        migrations.CreateModel(
            name='MealLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateTimeField()),
                ('meal_type', models.CharField(max_length=50)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal.patient')),
            ],
        ),
        migrations.CreateModel(
            name='FoodinMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal.food')),
                ('meal_log', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal.meallog')),
            ],
        ),
    ]