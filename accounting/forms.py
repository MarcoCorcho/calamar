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