from django.db import models

# Model Organizations


class ContactsInfo(models.Model):
    contact = models.CharField(max_length=100)              # ФИО
    customer_id = models.PositiveIntegerField()             # id кастомера, к которому привязан контакт
    type = models.PositiveIntegerField()                    # тип контакта
    created_dt = models.DateTimeField(auto_now_add=True)    # Дата создания записи
    updated_dt = models.DateTimeField(auto_now=True)        # Дата изменения записи
    uid = models.PositiveIntegerField(default=0)            # ИД пользователя, редактировавшего запись последним
