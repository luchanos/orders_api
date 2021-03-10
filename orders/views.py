from django.http import HttpResponse
import json

from orders.models import DeviceType, Organizations, Customers


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
        customer = Customers(fio=data["fio"],
                             position=data["position"],
                             organization_id=data["organization_id"])
        customer.full_clean()
        customer.save()
        return HttpResponse("OK")
