from django.db import models

# Create your models here.


class Contacts(models.Model):
    organization_phone = models.CharField(max_length=12)    # Телефон организации
    organization_email = models.CharField(max_length=100)   # Электронная почта организации
    organization_id = models.PositiveIntegerField()         # id организации
    description = models.CharField(max_length=255)          # Примечание
    created_dt = models.DateTimeField(auto_now_add=True)    # Дата создания записи
    updated_dt = models.DateTimeField(auto_now=True)        # Дата изменения записи
    uid = models.PositiveIntegerField(default=0)            # ИД пользователя, редактировавшего запись последним
