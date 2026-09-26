from django import forms
from .models import AccountType, Catalog, Period, AccountingEntryHeader, AccountingEntryDetail

# Create your forms here.

# Form for AccountType model
class AccountTypeForm(forms.ModelForm):
    description = forms.CharField(max_length=20, label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.BooleanField(required=False, label='Active', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = AccountType
        fields = ['description', 'status']

# Form for Catalog model
class CatalogForm(forms.ModelForm):
    code = forms.CharField(max_length=20, label='Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=100, label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.BooleanField(required=False, label='Active', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    parent = forms.ModelChoiceField(required=False, queryset=Catalog.objects.all(), empty_label="-- Select an account --", to_field_name="id", label="Parent Account")
    account_type = forms.ModelChoiceField(queryset=AccountType.objects.all(), empty_label="-- Select a Type --", to_field_name="id", required=True, label="Account Type")

    class Meta:
        model = Catalog
        fields = ['code','description', 'status', 'parent', 'account_type']
        
# Form for Period model
class PeriodForm(forms.ModelForm):
    description = forms.CharField(max_length=100, label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(required=True, label="Select start date", widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}))
    end_date = forms.DateField(required=True, label="Select end date", widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}))
    status = forms.BooleanField(required=False, label='Active', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Period
        fields =  ['description', 'start_date', 'end_date', 'status']
        
# Form for Accounting Entry Header Model
class AccountingEntryHeaderForm(forms.ModelForm):
    description = forms.CharField(max_length=100, label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))
    period = forms.ModelChoiceField(queryset=Period.objects.all(), empty_label="-- Select a Type --", to_field_name="id", required=True, label="Period")
    status = forms.BooleanField(required=False, label='Active', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = AccountingEntryHeader
        fields = ['description', 'period', 'status']
        
# Form for Accounting Entry Details Model
class AccoutingEntryDetailsForm(forms.ModelForm):
    accounting_entry_header = forms.ModelChoiceField(queryset=AccountingEntryHeader.objects.all(), empty_label="-- Select a Type --", to_field_name="id", required=True, label="Accounting Entry Header")
    catalog = forms.ModelChoiceField(queryset=Catalog.objects.all(), empty_label="-- Select a Type --", to_field_name="id", required=True, label="Catalog Account")
    debit = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01', 'min': '0'}))
    credit = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00', 'step': '0.01', 'min': '0'}))
    status = forms.BooleanField(required=False, label='Active', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = AccountingEntryDetail
        fields = ['accounting_entry_header', 'catalog', 'debit', 'credit', 'status']