from django.urls import path
from . import views

# Create your urls here.

urlpatterns = [
    path('configuration-menu/', views.configuration_menu, name='configuration_menu'),
    path('configuration-submenu/', views.configuration_submenu, name='configuration_submenu'),
    path('companies/', views.companies, name='companies'),
    path('add-company/', views.add_company, name='add_company'),
    path('edit-company/<int:company_id>/', views.edit_company, name='edit_company'),
    path('delete-company/<int:company_id>/', views.delete_company, name='delete_company'),
    path('outlets/', views.outlets, name='outlets'),
    path('add-outlet/', views.add_outlet, name='add_outlet'),
    path('edit-outlet/<int:outlet_id>/', views.edit_outlet, name='edit_outlet'),
    path('delete-outlet/<int:outlet_id>/', views.delete_outlet, name='delete_outlet'),
]