from django.shortcuts import render

# Create your views here.

# View for Services Contract Menu
def servicescontract_menu(request):
    template_name = 'servicescontract/servicescontract-menu.html'
    return render(request, template_name)

# View for Services Contract Submenu
def servicescontract_submenu(request):
    template_name = 'servicescontract/servicescontract-submenu.html'
    return render(request, template_name)