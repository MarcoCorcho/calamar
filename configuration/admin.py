from django.contrib import admin
from .models import Company, Outlet

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'email', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('name', 'email')
    readonly_fields = ('created_at', 'updated_at')

class OutletAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'address', 'phone_number', 'email', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('name', 'email')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Outlet, OutletAdmin)