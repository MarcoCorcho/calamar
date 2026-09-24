from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import AccountType, Catalog, Period, AccountingEntryHeader, AccountingEntryDetail
from .forms import AccountTypeForm, CatalogForm, PeriodForm
from django.template import loader
from django.contrib import messages

# Create your views here.

# View for Accounting Menu
def accounting_menu(request):
    template_name = 'accounting/accounting-menu.html'
    return render(request, template_name)

# View for Accounting Submenu
def accounting_submenu(request):
    template_name = 'accounting/accounting-submenu.html'
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

# View for Period
def periods(request):
    periods = Period.objects.all()
    template_name = 'accounting/periods.html'
    context = {
        'periods': periods,
    }
    return render(request, template_name, context)

# View to add new Period
def add_period(request):
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            status = form.cleaned_data['status']
            Period.objects.create(description=description, start_date=start_date, end_date=end_date, status=status)
            messages.success(request, 'Period added')
            return redirect('/accounting/periods/')
    else:
        form = PeriodForm()
        
    template = loader.get_template('accounting/add-period.html')
    context = {
       'form': form,
    }
    return HttpResponse(template.render(context, request))

# View to edit an existing Period
def edit_period(request, period_id):
    period = get_object_or_404(Period, id=period_id)
    if request.method == 'POST':
        form = PeriodForm(request.POST, instance=period)
        if form.is_valid():
            form.save()
            messages.success(request, 'Period updated')
            return redirect('/accounting/periods/')
    else:
        form = PeriodForm(instance=period)
    return render(request, 'accounting/edit-period.html', {'form': form, 'period': period})

# View to delete an existing Period
def delete_period(request, period_id):
    period = Period.objects.get(id=period_id)
    period.delete()
    return redirect('/accounting/periods/')