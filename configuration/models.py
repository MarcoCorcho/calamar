from django.db import models

# Create your models here.

# Model for Company
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Model for Outlet
class Outlet(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name