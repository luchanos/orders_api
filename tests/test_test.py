from django.test import Client
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_a():
    c = Client()
    js = {"device_type_code": 123, "device_type_name": "some analyzer"}
    res = c.post('/add_device_type/', js, content_type="application/json")
    assert res.status_code == 200


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_add_organization():
    c = Client()
    js = {"org_name": "ООО Рога и копыта", "org_address": "Тупичок Гоблина, 123", "org_city": "Мухосранск", "org_inn": 2100000000}
    res = c.post('/add_organization/', js, content_type="application/json")
    assert res.status_code == 200


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_add_contacts_info():
    c = Client()
    js = {"contact": "Иван Андреев", "customer_id": 543, "type": 2}
    res = c.post('/add_contacts_info/', js, content_type="application/json")
    assert res.status_code == 200


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_add_contact():
    c = Client()
    js = {"organization_phone": "89876543210", "organization_email": "my@mail.ml", "organization_id": 2, "description": "Some description"}
    res = c.post('/add_contact/', js, content_type="application/json")
    assert res.status_code == 200
