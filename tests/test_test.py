from django.test import Client
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_a():
    c = Client()
    a = {"device_type_code": 123, "device_type_name": "some analyzer"}
    res = c.post('/add_device_type/', a, content_type="application/json")
    d = 1


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_b():
    c = Client()
    a = {"device_type_code": 123, "device_type_name": "some analyzer"}
    res = c.post('/add_device_type/', a, content_type="application/json")
    d = 1