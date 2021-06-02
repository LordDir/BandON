from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('registration/', views.registration, name = 'registration'),
    path('profile/', views.profile, name = 'profile'),
    
]
