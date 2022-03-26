from django.urls import path
from coachapp.views import CustomerDetailAPI, DietAPI, ExerciseAPI, ExerciseTypeAPI, ScheduleAPI


urlpatterns = [
    path('etype/',ExerciseTypeAPI.as_view()),
    path('exercise/',ExerciseAPI.as_view()),
    path('diet/',DietAPI.as_view()),
    path('schedule/',ScheduleAPI.as_view()),
    path('customerdetail/',CustomerDetailAPI.as_view()),
    
    
]