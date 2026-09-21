from django import forms
from .models import AccountType, Catalog, Period, AccountingEntryHeader, AccountingEntryDetail

# Create your forms here.

# Form for AccountType model
class AccountTypeForm(forms.ModelForm):
    description = forms.CharField(max_length=100, label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.BooleanField(required=False, label='Active', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = AccountType
        fields = ['description', 'status']

# Form for Catalog model
class CatalogForm(forms.ModelForm):
    code = forms.CharField(max_length=20, label='Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=100, label='Description', widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.BooleanField(required=False, label='Active', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    parent = forms.ModelChoiceField(queryset=Catalog.objects.all(), empty_label="-- Select an account --", to_field_name="id", required=True, label="Parent account")
    account_type = forms.ModelChoiceField(queryset=AccountType.objects.all(), empty_label="-- Select a Type --", to_field_name="id", required=True, label="Account Type")

    class Meta:
        model = Catalog
        fields = ['code','description', 'status', 'parent', 'account_type']