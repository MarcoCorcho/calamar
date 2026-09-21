from django.db import models

# Create your models here.

# Account Type Model
class AccountType(models.Model):
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Account Type"
        verbose_name_plural = "Account Types"

    def __str__(self):
        return f"{self.description} ({'Active' if self.status else 'Inactive'})"


# Catalog Model
class Catalog(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE, related_name='catalogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Catalog"
        verbose_name_plural = "Catalogs"

    def __str__(self):
        return f"{self.description} ({'Active' if self.status else 'Inactive'})"


# Period Model
class Period(models.Model):
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Period"
        verbose_name_plural = "Periods"

    def __str__(self):
        return f"{self.description} ({'Active' if self.status else 'Inactive'})"


# Accouting Entry Header Model
class AccountingEntryHeader(models.Model):
    description = models.CharField(max_length=100)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='accounting_entry_headers')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Accounting Entry Header"
        verbose_name_plural = "Accounting Entry Headers"

    def __str__(self):
        return f"{self.description} ({'Active' if self.status else 'Inactive'})"


# Accounting Entry Detail Model
class AccountingEntryDetail(models.Model):
    accounting_entry_header = models.ForeignKey(AccountingEntryHeader, on_delete=models.CASCADE, related_name='accounting_entry_details')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='accounting_entry_details')
    debit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Accounting Entry Detail"
        verbose_name_plural = "Accounting Entry Details"

    def __str__(self):
        return f"Detail for {self.accounting_entry_header.description} - {self.catalog.description} ({'Active' if self.status else 'Inactive'})"