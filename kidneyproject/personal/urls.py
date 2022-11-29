from django.urls import path
from .views import indexPageView, foodJournalView, addFoodView, levelsLogView, addLevelView, deleteLogView

urlpatterns = [
    path('', indexPageView, name="index"),
    path('journal/', foodJournalView, name="journal"),
    path('add-food/', addFoodView, name="add-food"),
    path('log/', levelsLogView, name="log"),
    path('add-level', addLevelView, name="add-level"),
    path("deleteLog/<int:type>+<int:pat>/", deleteLogView, name="deleteLog"),
]