from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'personal/index.html')

def foodJournalView(request) :
    return render(request, 'personal/journal.html')

def addFoodView(request) :
    return render(request, 'personal/food.html')

def levelsLogView(request) :
    return render(request, 'personal/serumlevels.html')

def addLevelView(request) :
    return render(request, 'personal/serumlevels.html')