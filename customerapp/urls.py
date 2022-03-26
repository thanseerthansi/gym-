from django.urls import path

from customerapp.views import D_planGetAPI, ExerciseGetAPI, ScheduleGetAPI, customerGetAPI



urlpatterns = [
    path('customer/',customerGetAPI.as_view()),
    path('d_plan/',D_planGetAPI.as_view()),
    path('schedule/',ScheduleGetAPI.as_view()),
    path('exercise/',ExerciseGetAPI.as_view()),
   
    
    
]