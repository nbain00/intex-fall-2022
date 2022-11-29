from django.urls import path
from .views import indexPageView, foodJournalView, addFoodView, levelsLogView, addLevelView, deleteLogView
from .views import profileEditView
urlpatterns = [
    path('', indexPageView, name="index"),
    path('journal/', foodJournalView, name="journal"),
    path('add-food/', addFoodView, name="add-food"),
    path('log/', levelsLogView, name="log"),
    path('add-level/', addLevelView, name="add-level"),
    path("deleteLog/<int:type>+<int:pat>/", deleteLogView, name="deleteLog"),
    path("showProfile/<int:userid>", profileEditView, name="showProfile"),
]