from django.db import models
from configuration.models import Outlet
from accounting.models import AccountingEntryHeader, AccountingEntryDetail

# Create your models here.

# Model for Area
class Area(models.Model):
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    verbose_name = "Area"
    verbose_name_plural = "Areas"

    def __str__(self):
        return self.name

# Model for Advertising Space
class AdvertisingSpace(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    width = models.FloatField()
    height = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    verbose_name = "Advertising Space"
    verbose_name_plural = "Advertising Spaces"

    def __str__(self):
        return self.name
    
# Model for Client
class Client(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    client_account = models.ForeignKey(AccountingEntryHeader, on_delete=models.CASCADE, related_name='clients')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    verbose_name = "Client"
    verbose_name_plural = "Clients"

    def __str__(self):
        return self.name
    
# Model for Contract Header
class ContractHeader(models.Model):
    #advertising_space = models.ForeignKey(AdvertisingSpace, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_name')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    debit_note = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    verbose_name = "Contract Header"
    verbose_name_plural = "Contract Headers"
    
    def __str__(self):
        return f"Contract for {self.advertising_space.name} from {self.start_date} to {self.end_date} status: {'Active' if self.status else 'Inactive'} debit_note: {'Yes' if self.debit_note else 'No'}"
    
# Model for Contract Detail
class ContractDetail(models.Model):
    contract_header = models.ForeignKey(ContractHeader, on_delete=models.CASCADE)
    advertising_space = models.ForeignKey(AdvertisingSpace, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.ForeignKey(AdvertisingSpace, on_delete=models.CASCADE, related_name='unit_price')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    verbose_name = "Contract Detail"
    verbose_name_plural = "Contract Details"

    def __str__(self):
        return f"Detail for {self.contract_header.advertising_space.name} - {self.advertising_space.name} (Quantity: {self.quantity}, Total Price: {self.total_price})"