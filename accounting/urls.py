from django.urls import path
from . import views

# Create your urls here.

urlpatterns = [
    path('menu/', views.accounting_menu, name='accounting_menu'),
    path('account-types/', views.account_types, name='account_types'),
]