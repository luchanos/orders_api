from django.db import models


# Create your models here.
class Equipment(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='дата создания записи')
    updated_dt = models.DateTimeField(auto_now=True, verbose_name='дата обновления информации')
    serial_no = models.TextField(blank=True, verbose_name='серийный номер')
    type_id = models.IntegerField(blank=True, verbose_name='тип оборудования')
    manufacturer_id = models.IntegerField(blank=True, verbose_name='id производителя')
    organization_id = models.IntegerField(blank=True, verbose_name='id организации, которой принадлежит оборудование')

    def __str__(self):
        self.serial_no

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
