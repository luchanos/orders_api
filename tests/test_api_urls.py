from django.test import Client
import pytest

from orders.models import Customers, DeviceType, Organizations


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_add_device_type():
    test_cli = Client()
    js = {"device_type_code": 123, "device_type_name": "some analyzer"}
    res = test_cli.post('/add_device_type/', js, content_type="application/json")
    assert res.status_code == 200
    data_from_db = DeviceType.objects.all()
    assert len(data_from_db) == 1
    record = data_from_db[0]
    assert record.device_type_code == js["device_type_code"]
    assert record.device_type_name == js["device_type_name"]


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_add_organization():
    test_cli = Client()
    js = {"organization_name": "ООО Рога и копыта",
          "address": "Мухосранск, Тупичок Гоблина, 123"}
    res = test_cli.post('/add_organization/', js, content_type="application/json")
    assert res.status_code == 200
    data_from_db = Organizations.objects.all()
    assert len(data_from_db) == 1
    record = data_from_db[0]
    assert record.organization_name == js["organization_name"]
    assert record.address == js["address"]
