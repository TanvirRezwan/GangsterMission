from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_checked_out = models.BooleanField(default=False)
    condition = models.CharField(max_length=100)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    checked_out_date = models.DateTimeField(null=True, blank=True)
    returned_date = models.DateTimeField(null=True, blank=True)
