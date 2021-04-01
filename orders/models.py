from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


class DeviceType(models.Model):
    """Модель для типа оборудования"""
    device_type_code = models.IntegerField(unique=True, validators=[MinValueValidator(1), ])
    device_type_name = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(1), ])


class Organizations(models.Model):
    """Модель для организаций"""
    organization_name = models.TextField(unique=True, validators=[MinLengthValidator(1), ])
    address = models.TextField(validators=[MinLengthValidator(1), ])


class Customers(models.Model):
    """Модель для представителей контрагентов"""
    fio = models.CharField(max_length=100, validators=[MinLengthValidator(3), ])
    position = models.CharField(max_length=100, validators=[MinLengthValidator(1), ])
    organization_id = models.ForeignKey(Organizations, on_delete=models.CASCADE)
