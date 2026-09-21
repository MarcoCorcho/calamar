from django.urls import path
from . import views

# Create your urls here.

urlpatterns = [
    path('menu/', views.accounting_menu, name='accounting_menu'),
    path('account-types/', views.account_types, name='account_types'),
    path('add-account-type/', views.add_account_type, name='add_account_type'),
    path('edit-account-type/<int:account_type_id>/', views.edit_account_type, name='edit_account_type'),
    path('delete-account-type/<int:account_type_id>/', views.delete_account_type, name='delete_account_type'),
    path('catalogs/', views.catalogs, name='catalogs'),
    path('add-catalog/', views.add_catalog, name='add_catalog'),
]