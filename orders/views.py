from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from orders.models import EquipmentTypes


@csrf_exempt
def add_equipment_type(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_equipment_type = EquipmentTypes\
            (type_name=data['type_name'],
             description=data['description'],)
        EquipmentTypes.save(new_equipment_type)
        return HttpResponse('OK')
