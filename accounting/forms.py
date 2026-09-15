from django.forms import forms
from .models import AccountType, Catalog, Period, AccountingEntryHeader, AccountingEntryDetail

# Create your forms here.

# Form for AccountType model
class AccountTypeForm(forms.ModelForm):
    description = forms.CharField(max_length=100, required=True, label='Description')
    status = forms.BooleanField(required=False, initial=True, label='Status')


