from django.urls import path
from . import views

# Create your urls here.

urlpatterns = [
    path('servicescontract-menu/', views.servicescontract_menu, name='servicescontract_menu'),
    path('servicescontract-submenu/', views.servicescontract_submenu, name='servicescontract_submenu'),
]