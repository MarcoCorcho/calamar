from django.urls import path
from . import views

# Create your urls here.

urlpatterns = [
    path('servicescontract-menu/', views.servicescontract_menu, name='servicescontract_menu'),
    path('servicescontract-submenu/', views.servicescontract_submenu, name='servicescontract_submenu'),
    path('areas/', views.areas, name='areas'),
    path('add-area/', views.add_area, name='add_area'),
    path('edit-area/<int:area_id>/', views.edit_area, name='edit_area'),
    path('delete-area/<int:area_id>/', views.delete_area, name='delete_area'),
    path('advertising-spaces/', views.advertising_spaces, name='advertising_spaces'),
    path('add-advertising-space/', views.add_advertising_space, name='add_advertising_space'),
    path('edit-advertising-space/<int:advertising_space_id>/', views.edit_advertising_space, name='edit_advertising_space'),
    path('delete-advertising-space/<int:advertising_space_id>/', views.delete_advertising_space, name='delete_advertising_space'),
]