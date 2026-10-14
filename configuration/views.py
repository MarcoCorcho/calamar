from django.shortcuts import redirect, render, get_object_or_404
from .models import Company, Outlet, CompanyCatalog
from django.http import HttpResponse
from .forms import CompanyForm, OutletForm, CompanyCatalogForm
from django.contrib import messages

# Create your views here.

# View for Configuration Menu
def configuration_menu(request):
    template_name = 'configuration/configuration-menu.html'
    return render(request, template_name)

# View for Configuration Submenu
def configuration_submenu(request):
    template_name = 'configuration/configuration-submenu.html'
    return render(request, template_name)

# View to list all companies
def companies(request):
    companies = Company.objects.all()
    template_name = 'configuration/companies.html'
    context = {'companies': companies}
    return render(request, template_name, context)

# View to add a new company
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company added')
            return redirect('companies')
    else:
        form = CompanyForm()
    return render(request, 'configuration/add-company.html', {'form': form})

# View to edit an existing company
def edit_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company updated')
            return redirect('companies')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'configuration/edit-company.html', {'form': form, 'company': company})

# View to delete a company
def delete_company(request, company_id):
    company = Company.objects.get(id=company_id)
    company.delete()
    messages.success(request, 'Company deleted')
    return redirect('/configuration/companies/')

# View to list all outlets
def outlets(request):
    outlets = Outlet.objects.all()
    template_name = 'configuration/outlets.html'
    context = {'outlets': outlets}
    return render(request, template_name, context)

# View to add a new outlet
def add_outlet(request):
    if request.method == 'POST':
        form = OutletForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Outlet added')
            return redirect('outlets')
    else:
        form = OutletForm()
    return render(request, 'configuration/add-outlet.html', {'form': form})

# View to edit an existing outlet
def edit_outlet(request, outlet_id):
    outlet = get_object_or_404(Outlet, id=outlet_id)
    if request.method == 'POST':
        form = OutletForm(request.POST, instance=outlet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Outlet updated')
            return redirect('outlets')
    else:
        form = OutletForm(instance=outlet)
    return render(request, 'configuration/edit-outlet.html', {'form': form, 'outlet': outlet})

# View to delete an outlet
def delete_outlet(request, outlet_id):
    outlet = Outlet.objects.get(id=outlet_id)
    outlet.delete()
    messages.success(request, 'Outlet deleted')
    return redirect('/configuration/outlets/')

# View to list all company catalogs
def company_catalogs(request):
    company_catalogs = CompanyCatalog.objects.all()
    template_name = 'configuration/company-catalogs.html'
    context = {'company_catalogs': company_catalogs}
    return render(request, template_name, context)

# View to add a new company catalog
def add_company_catalog(request):
    if request.method == 'POST':
        form = CompanyCatalogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company Catalog added')
            return redirect('company_catalogs')
    else:
        form = CompanyCatalogForm()
    return render(request, 'configuration/add-company-catalog.html', {'form': form})

# View to edit an existing company catalog
def edit_company_catalog(request, company_catalog_id):
    company_catalog = get_object_or_404(CompanyCatalog, id=company_catalog_id)
    if request.method == 'POST':
        form = CompanyCatalogForm(request.POST, instance=company_catalog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company Catalog updated')
            return redirect('company_catalogs')
    else:
        form = CompanyCatalogForm(instance=company_catalog)
    return render(request, 'configuration/edit-company-catalog.html', {'form': form, 'company_catalog': company_catalog})

# View to delete a company catalog
def delete_company_catalog(request, company_catalog_id):
    company_catalog = CompanyCatalog.objects.get(id=company_catalog_id)
    company_catalog.delete()
    messages.success(request, 'Company Catalog deleted')
    return redirect('/configuration/company-catalogs/')