from django.contrib import admin
from .models import AccountType, Catalog, Period, AccountingEntryHeader, AccountingEntryDetail

# Register your models here.
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('description', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('description',)
    readonly_fields = ('created_at', 'updated_at')

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('description', 'status', 'parent', 'account_type', 'created_at', 'updated_at')
    list_filter = ('status', 'account_type')
    search_fields = ('description',)
    readonly_fields = ('created_at', 'updated_at')

class PeriodAdmin(admin.ModelAdmin):
    list_display = ('description', 'start_date', 'end_date', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('description',)
    readonly_fields = ('created_at', 'updated_at')

class AccountingEntryHeaderAdmin(admin.ModelAdmin):
    list_display = ('description', 'period', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'period')
    search_fields = ('description',)
    readonly_fields = ('created_at', 'updated_at')

class AccountingEntryDetailAdmin(admin.ModelAdmin):
    list_display = ('accounting_entry_header', 'catalog', 'debit', 'credit', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('accounting_entry_header__description', 'catalog__description')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Period, PeriodAdmin)
admin.site.register(AccountingEntryHeader, AccountingEntryHeaderAdmin)
admin.site.register(AccountingEntryDetail, AccountingEntryDetailAdmin)