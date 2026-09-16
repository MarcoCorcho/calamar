from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import AccountType, Catalog, Period, AccountingEntryHeader, AccountingEntryDetail
from .forms import AccountTypeForm
from django.template import loader
from django.contrib import messages

# Create your views here.

# View for Accounting Menu
def accounting_menu(request):
    template_name = 'accounting/accounting-menu.html'
    return render(request, template_name)

# View for Account Types
def account_types(request):
    account_types = AccountType.objects.all()
    template_name = 'accounting/account-types.html'
    context = {
        'account_types': account_types,
    }
    return render(request, template_name, context)

# View to add a new Account Type
def add_account_type(request):
    if request.method == 'POST':
        form = AccountTypeForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            AccountType.objects.create(description=description, status=status)
            messages.success(request, 'Account Type added')
            return redirect('/accounting/account-types/')
    else:
        form = AccountTypeForm()
    
    template = loader.get_template('accounting/add-account-type.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# View to edit an existing Account Type
def edit_account_type(request, account_type_id):
    account_type = get_object_or_404(AccountType, id=account_type_id)
    if request.method == 'POST':
        form = AccountTypeForm(request.POST, instance=account_type)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Type updated')
            return redirect('/accounting/account-types/')
    else:
        form = AccountTypeForm(instance=account_type)
    return render(request, 'accounting/edit-account-type.html', {'form': form, 'account_type': account_type})

# View to delete an existing Account Type
def delete_account_type(request, account_type_id):
    account_type = AccountType.objects.get(id=account_type_id)
    account_type.delete()
    return redirect('/accounting/account-types/')