from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import AccountType, Catalog, Period, AccountingEntryHeader, AccountingEntryDetail
from .forms import AccountTypeForm, CatalogForm
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

# View for Catalog
def catalogs(request):
    catalogs = Catalog.objects.all()
    template_name = 'accounting/catalogs.html'
    context = {
        'catalogs': catalogs,
    }
    return render(request, template_name, context)

# View to add new Catalog
def add_catalog(request):
    if request.method == 'POST':
        form = CatalogForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            description = form.cleaned_data['description']
            status = form.cleaned_data['status']
            parent = form.cleaned_data['parent']
            account_type = form.cleaned_data['account_type']
            Catalog.objects.create(code=code, description=description, status=status, parent=parent, account_type=account_type)
            messages.success(request, 'Catalog added')
            return redirect('/accounting/catalogs/')
    else:
        form = CatalogForm()
        
    template = loader.get_template('accounting/add-catalog.html')
    context = {
       'form': form,
    }
    return HttpResponse(template.render(context, request))

# View to edit an existing Catalog
def edit_catalog(request, catalog_id):
    catalog = get_object_or_404(Catalog, id=catalog_id)
    if request.method == 'POST':
        form = CatalogForm(request.POST, instance=catalog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Catalog account updated')
            return redirect('/accounting/catalogs/')
    else:
        form = CatalogForm(instance=catalog)
    return render(request, 'accounting/edit-catalog.html', {'form': form, 'catalog': catalog})

# View to delete an existing Catalog
def delete_catalog(request, catalog_id):
    catalog = Catalog.objects.get(id=catalog_id)
    catalog.delete()
    return redirect('/accounting/catalogs/')