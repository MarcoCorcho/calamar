from django.shortcuts import render
from .models import AccountType, Catalog, Period, AccountingEntryHeader, AccountingEntryDetail

# Create your views here.

# View for Accounting Menu
def accounting_menu(request):
    template_name = 'accounting/accounting_menu.html'
    return render(request, template_name)

# View for Account Types
def account_types(request):
    account_types = AccountType.objects.all()
    template_name = 'accounting/account_types.html'
    context = {
        'account_types': account_types,
    }
    return render(request, template_name, context)