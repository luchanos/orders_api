from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt  # для корректной работы POST
import json

from orders.models import Equipment

# Create your views here.


@csrf_exempt
def add_equipment(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # вытаскиваем данные и преобразуем в словарь
        print(data)
        new_equipment = Equipment(
            serial_no=data['serial_no'],
            type_id=data['type_id'],
            manufacturer_id=data['manufacturer_id'],
            organization_id=data['organization_id'],
            model_id=data['model_id'],
            uid=data['uid']
        )
        Equipment.save(new_equipment)
        return HttpResponse("OK")
    else:
        return HttpResponse("YOU MUST USE POST METHOD!")
