from django.urls import path
from . import views

# Create your urls here.

urlpatterns = [
    path('accounting-menu/', views.accounting_menu, name='accounting_menu'),
    path('accounting-submenu/', views.accounting_submenu, name='accounting_submenu'),
    path('account-types/', views.account_types, name='account_types'),
    path('add-account-type/', views.add_account_type, name='add_account_type'),
    path('edit-account-type/<int:account_type_id>/', views.edit_account_type, name='edit_account_type'),
    path('delete-account-type/<int:account_type_id>/', views.delete_account_type, name='delete_account_type'),
    path('catalogs/', views.catalogs, name='catalogs'),
    path('add-catalog/', views.add_catalog, name='add_catalog'),
    path('edit-catalog/<int:catalog_id>/', views.edit_catalog, name='edit_catalog'),
    path('delete-catalog/<int:catalog_id>/', views.delete_catalog, name='delete_catalog'),
    path('periods/', views.periods, name='periods'),
    path('add-period/', views.add_period, name='add_period'),
    path('edit-period/<int:period_id>/', views.edit_period, name='edit_period'),
    path('delete-period/<int:period_id>/', views.delete_period, name='delete_period'),
    path('accounting-entry-headers/', views.accounting_entry_headers, name='accounting_entry_headers'),
    path('add-accounting-entry-header/', views.add_accouting_entry_header, name='add_accounting_entry_header'),
]