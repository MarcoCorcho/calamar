from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Area, AdvertisingSpace, Client, ContractHeader
from .forms import AreaForm, AdvertisingSpaceForm, ClientForm, ContractHeaderForm

# Create your views here.

# View for Services Contract Menu
def servicescontract_menu(request):
    template_name = 'servicescontract/servicescontract-menu.html'
    return render(request, template_name)

# View for Services Contract Submenu
def servicescontract_submenu(request):
    template_name = 'servicescontract/servicescontract-submenu.html'
    return render(request, template_name)

# View for Areas
def areas(request):
    areas = Area.objects.all()
    template_name = 'servicescontract/areas.html'
    context = {'areas': areas}
    return render(request, template_name, context)