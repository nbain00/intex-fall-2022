from django.urls import path
from .views import indexPageView, foodJournalView, addFoodView, levelsLogView, addLevelView, deleteLogView
from .views import profileEditView
urlpatterns = [
    path('', indexPageView, name="index"),
    path('journal/<int:userid>/', foodJournalView, name="journal"),
    path('add-food/<int:userid>', addFoodView, name="add-food"),
    path('log/<int:userid>', levelsLogView, name="log"),
    path('add-level/<int:userid>', addLevelView, name="add-level"),
    path("deleteLog/<int:userid>/<int:logid>/", deleteLogView, name="deleteLog"),
    path("showProfile/<int:userid>/", profileEditView, name="showProfile"),
]