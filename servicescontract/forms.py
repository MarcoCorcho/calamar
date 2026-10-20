from django import forms
from django.forms.models import BaseInlineFormSet
from accounting.models import AccountingEntryHeader
from configuration.models import Outlet
from .models import Area, AdvertisingSpace, Client, ContractHeader, ContractDetail

# Form for Area
class AreaForm(forms.ModelForm):
    outlet = forms.ModelChoiceField(queryset=Outlet.objects.all(), label='Outlet', required=True)
    name = forms.CharField(max_length=200, label='Area Name', required=True)
    description = forms.CharField(widget=forms.Textarea, label='Description', required=True)
    status = forms.BooleanField(label='Status', required=False, initial=True)
    class Meta:
        model = Area
        fields = ['outlet', 'name', 'description', 'status']
        
# Form for Advertising Space
class AdvertisingSpaceForm(forms.ModelForm):
    area = forms.ModelChoiceField(queryset=Area.objects.all(), label='Area', required=True)
    name = forms.CharField(max_length=200, label='Advertising Space Name', required=True)
    description = forms.CharField(widget=forms.Textarea, label='Description', required=True)
    width = forms.FloatField(label='Width', required=True)
    height = forms.FloatField(label='Height', required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Price', required=True)
    status = forms.BooleanField(label='Status', required=False, initial=True)
    
    class Meta:
        model = AdvertisingSpace
        fields = ['area', 'name', 'description', 'width', 'height', 'price', 'status']
        
# Form for Client
class ClientForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label='Client Name', required=True)
    description = forms.CharField(widget=forms.Textarea, label='Description', required=True)
    client_account = forms.ModelChoiceField(queryset=AccountingEntryHeader.objects.all(), label='Client Account', required=True)
    status = forms.BooleanField(label='Status', required=False, initial=True)

    class Meta:
        model = Client
        fields = ['name', 'description', 'client_account', 'status']
        
# Form for Contract Header
class ContractHeaderForm(forms.ModelForm):
    advertising_space = forms.ModelChoiceField(queryset=AdvertisingSpace.objects.all(), label='Advertising Space', required=True)
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Client', required=True)
    start_date = forms.DateField(widget=forms.SelectDateWidget, label='Start Date', required=True)
    end_date = forms.DateField(widget=forms.SelectDateWidget, label='End Date', required=True)
    total_price = forms.DecimalField(max_digits=10, decimal_places=2, label='Total Price', required=True)
    status = forms.BooleanField(label='Status', required=False, initial=True)
    debit_note = forms.BooleanField(label='Debit Note', required=False, initial=False)
    
    class Meta:
        model = ContractHeader
        fields = ['advertising_space', 'client', 'start_date', 'end_date', 'total_price', 'status', 'debit_note']
        
# Class for Base Accounting Entry Details Model
class BaseContractDetailFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        # El argumento 'instance' representa el registro padre (Header)
        instance = kwargs.get('instance', None)
        
        # Si la instancia ya existe en la base de datos (tiene ID), no agregamos líneas extra
        if instance and instance.pk:
            self.extra = 0
            
        super().__init__(*args, **kwargs)
        
# Formset for Contract Detail Model
#ContractDetailFormSet = forms.inlineformset_factory(
#    ContractHeader,
#    AdvertisingSpace,
#    fields=['quantity', 'total_price'],
#    formset=BaseContractDetailFormSet,
#    extra=1,
#    can_delete=True
#)