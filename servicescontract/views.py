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

# View for creating a new Area
def add_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Area created successfully.')
            return redirect('areas')
    else:
        form = AreaForm()
    return render(request, 'servicescontract/add-area.html', {'form': form})

# View for editing an Area
def edit_area(request, area_id):
    area = get_object_or_404(Area, id=area_id)
    if request.method == 'POST':
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            messages.success(request, 'Area updated successfully.')
            return redirect('areas')
    else:
        form = AreaForm(instance=area)
    return render(request, 'servicescontract/edit-area.html', {'form': form, 'area': area})

# View for deleting an Area
def delete_area(request, area_id):
    area = Area.objects.get(id=area_id)
    area.delete()
    messages.success(request, 'Area deleted successfully.')
    return redirect('/servicescontract/areas/')

# View for Advertising Spaces
def advertising_spaces(request):
    advertising_spaces = AdvertisingSpace.objects.all()
    template_name = 'servicescontract/advertising-spaces.html'
    context = {'advertising_spaces': advertising_spaces}
    return render(request, template_name, context)

# View for creating a new Advertising Space
def add_advertising_space(request):
    if request.method == 'POST':
        form = AdvertisingSpaceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Advertising Space created successfully.')
            return redirect('advertising_spaces')
    else:
        form = AdvertisingSpaceForm()
    return render(request, 'servicescontract/add-advertising-space.html', {'form': form})

# View for editing an Advertising Space
def edit_advertising_space(request, advertising_space_id):
    advertising_space = get_object_or_404(AdvertisingSpace, id=advertising_space_id)
    if request.method == 'POST':
        form = AdvertisingSpaceForm(request.POST, instance=advertising_space)
        if form.is_valid():
            form.save()
            messages.success(request, 'Advertising Space updated successfully.')
            return redirect('advertising_spaces')
    else:
        form = AdvertisingSpaceForm(instance=advertising_space)
    return render(request, 'servicescontract/edit-advertising-space.html', {'form': form, 'advertising_space': advertising_space})

#View for deleting an Advertising Space
def delete_advertising_space(request, advertising_space_id):
    advertising_space = AdvertisingSpace.objects.get(id=advertising_space_id)
    advertising_space.delete()
    messages.success(request, 'Advertising Space deleted successfully.')
    return redirect('/servicescontract/advertising-spaces/')