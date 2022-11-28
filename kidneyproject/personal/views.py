from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'base.html')

def foodJournalView(request) :
    return HttpResponse('This will be the food journal page')

def addFoodView(request) :
    return HttpResponse('Page for adding new food')

def levelsLogView(request) :
    return HttpResponse('This page will have serum levels info')

def addLevelView(request) :
    return HttpResponse('Page for adding serum levels')