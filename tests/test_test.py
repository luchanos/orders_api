from django.test import Client
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_add_equipment():
    client = Client()
    content = {"serial_no": "tghgfhf", "type_id": 1, "manufacturer_id": 1, "organization_id": 1}
    res = client.post('/orders/add_equipment/',
                      content,
                      content_type='application/json')
    assert res.status_code == 200


