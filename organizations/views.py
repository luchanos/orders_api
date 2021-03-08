import json

from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from organizations.models import Organization


@csrf_exempt
def add_organization(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_organization = Organization(org_name=data['org_name'],  # Название организации
                                        org_address=data['org_address'],  # Адрес организации
                                        org_city=data['org_city'],  # Город организации
                                        org_inn=data['org_inn'],  # ИНН организации
                                        )
        Organization.save(new_organization)
        return HttpResponse("OK")
