from django.http import HttpResponse
import json


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from orders.models import DeviceType


# todo luchanos ЭТО ТЕСТОВАЯ ВЬЮХА, ЧИСТО ПОКАЗАТЬ КАК РАБОТАЕТ РУЧКА
@csrf_exempt
def add_device_type(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_device_model = DeviceType(device_type_code=data["device_type_code"],
                                      device_type_name=data["device_type_name"],
                                      )
        DeviceType.save(new_device_model)
        return HttpResponse("OK")
