from django.urls import path
from . import views

# Create your urls here.

urlpatterns = [
    path('configuration-menu/', views.configuration_menu, name='configuration_menu'),
    path('configuration-submenu/', views.configuration_submenu, name='configuration_submenu'),
    path('companies/', views.companies, name='companies'),
    path('add-company/', views.add_company, name='add_company'),
    path('edit-company/<int:company_id>/', views.edit_company, name='edit_company')
]