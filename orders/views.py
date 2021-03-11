from django.http import HttpResponse
import json


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from orders.models import EquipmentManufacturer


#
@csrf_exempt
def add_equipment_manufacturer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_equipment_manufacturer = EquipmentManufacturer(manufacturer_name=data['manufacturer_name'],
                                                           uid=['uid'],
                                                           description=['description'])
        EquipmentManufacturer.save(new_equipment_manufacturer)
        return HttpResponse('OK')
    else:
        return HttpResponse("YOU MUST USE POST METHOD!")

