from django.db import models


# Model Organizations

class Organization(models.Model):
    org_name = models.CharField(max_length=100)             # Название организации
    org_address = models.CharField(max_length=200)          # Адрес организации
    org_city = models.CharField(max_length=50)              # Город организации
    org_inn = models.PositiveBigIntegerField()              # ИНН организации
    created_dt = models.DateTimeField(auto_now_add=True)    # Дата создания записи
    updated_dt = models.DateTimeField(auto_now=True)        # Дата изменения записи
    uid = models.PositiveIntegerField(default=0)            # ИД пользователя, редактировавшего запись последним
