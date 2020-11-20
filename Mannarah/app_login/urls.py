from django.urls import path
from . import views

app_name = 'app_login'

urlpatterns = [
    path('signup/', views.signUpView, name="signup"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('', views.homeView, name="home"),
]