from django.urls import path

from loginapp.views import LoginView, Logout, UserAPI, WhoAmI



urlpatterns = [
    path('user/',UserAPI.as_view()),
    path('whoami/',WhoAmI.as_view()),
    path('log/',LoginView.as_view()),
    path('logout/',Logout.as_view()),
   
   
    
    
]