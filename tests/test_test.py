from django.test import Client
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_a():
    c = Client()
    js = {"device_type_code": 123, "device_type_name": "some analyzer"}
    res = c.post('/add_device_type/', js, content_type="application/json")
    assert res.status_code == 200
