from django.shortcuts import redirect, render, get_object_or_404
from .models import Company
from django.http import HttpResponse
from .forms import CompanyForm
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