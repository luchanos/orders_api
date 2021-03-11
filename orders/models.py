from django.db import models


# Create your models here.
class EquipmentManufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=50, blank=True, verbose_name='Имя производителя')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='дата создания записи')
    updated_dt = models.DateTimeField(auto_now=True, verbose_name='дата обновления информации')
    uid = models.IntegerField(blank=True, default=0, verbose_name='id пользователя создавшего или изменившего запись')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

