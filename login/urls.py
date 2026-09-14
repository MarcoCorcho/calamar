from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    #path('login/', auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
    #path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]