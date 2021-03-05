from django.test import Client
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_add_equipment():
    client = Client()
    content = {"serial_no": "sdfdsf",
               "type_id": 2,
               "model_id": 662,
               "manufacturer_id": 67,
               "organization_id": 2,
               "uid": 0}
    res = client.post('/orders/add_equipment/',
                      content,
                      content_type='application/json')
    assert res.status_code == 200
