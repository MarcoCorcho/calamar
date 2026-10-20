from django.contrib import admin
from .models import Area, AdvertisingSpace, Client, ContractHeader, ContractDetail

# Register your models here.

class AreaAdmin(admin.ModelAdmin):
    list_display = ('outlet', 'name', 'description', 'created_at', 'updated_at')
    list_filter = ('outlet',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

class AdvertisingSpaceAdmin(admin.ModelAdmin):
    list_display = ('area', 'name', 'description', 'width', 'height', 'price', 'created_at', 'updated_at')
    list_filter = ('area',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'client_account', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

class ContractHeaderAdmin(admin.ModelAdmin):
    list_display = ('client', 'start_date', 'end_date', 'total_price', 'status', 'debit_note', 'created_at', 'updated_at')
    list_filter = ('client', 'status', 'debit_note')
    search_fields = ('client__name', 'status')
    readonly_fields = ('created_at', 'updated_at')

class ContractDetailAdmin(admin.ModelAdmin):
    list_display = ('contract_header', 'advertising_space', 'quantity', 'unit_price', 'total_price', 'created_at', 'updated_at')
    list_filter = ('contract_header',)
    search_fields = ('advertising_space__name',)
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Area, AreaAdmin)
admin.site.register(AdvertisingSpace, AdvertisingSpaceAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ContractHeader, ContractHeaderAdmin)
admin.site.register(ContractDetail, ContractDetailAdmin)