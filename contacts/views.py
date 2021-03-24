import json

from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from contacts.models import Contacts


@csrf_exempt
def add_contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_contact = Contacts(organization_phone=data['organization_phone'],  # Телефон организации
                               organization_email=data['organization_email'],  # Электронная почта организации
                               organization_id=data['organization_id'],  # id организации
                               description=data['description']  # Примечание
                               )
        Contacts.save(new_contact)
        return HttpResponse("OK")
