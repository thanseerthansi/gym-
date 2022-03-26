from django.urls import path
from managerapp.views import *

urlpatterns = [
    path('plan/',SubscriptionAPI.as_view()),
    path('coach/',CoachAPI.as_view()),
    path('cutomer/',CustomerAPI.as_view()),
    
    
]
