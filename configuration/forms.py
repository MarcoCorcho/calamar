from django import forms
from .models import Company, Outlet

# Create your forms here.

# Form for Company
class CompanyForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    status = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Company
        fields = ['name', 'address', 'phone_number', 'email', 'status']
        
# Form for Outlet
class OutletForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.filter(status=True), empty_label="-- Select a Company --", to_field_name="id", required=True, label="Company")
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    status = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Outlet
        fields = ['company', 'name', 'address', 'phone_number', 'email', 'status']