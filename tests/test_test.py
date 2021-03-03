from django.test import Client
import pytest


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_add_equipment_type():
    c = Client()
    js = {
        'type_name': 'printer',
        'description': 'prints black letters on white paper'
    }
    res = c.post('/orders/add_equipment_type/', js, content_type="application/json")
    assert res.status_code == 200

