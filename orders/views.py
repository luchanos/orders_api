from django.http import HttpResponse
import json

from orders.models import DeviceType, Organizations, Customers, Manufacturer


def add_device_type(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_device_type = DeviceType(device_type_code=data["device_type_code"],
                                     device_type_name=data["device_type_name"])
        new_device_type.full_clean()
        new_device_type.save()
        return HttpResponse("OK")


def add_organization(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        organization = Organizations(organization_name=data["organization_name"],
                                     address=data["address"])
        organization.full_clean()
        organization.save()
        return HttpResponse("OK")


def add_customer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        organization = Organizations.objects.get(pk=data["organization_id"])
        customer = Customers(fio=data["fio"],
                             position=data["position"],
                             organization_id=organization)
        customer.full_clean()  # для применения валидации
        customer.save()
        return HttpResponse("OK")


def add_equipment_manufacturer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        equipment_manufacturer = Manufacturer(manufacturer_name=data['manufacturer_name'],
                                              uid=['uid'],
                                              description=['description'])
        equipment_manufacturer.full_clean()
        equipment_manufacturer.save()
        return HttpResponse('OK')
