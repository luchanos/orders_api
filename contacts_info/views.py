import json

from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from contacts_info.models import ContactsInfo


@csrf_exempt
def add_contacts_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_contact_info = ContactsInfo(contact=data['contact'],  # ФИО
                                        customer_id=data['customer_id'],  # id кастомера, к которому привязан контакт
                                        type=data['type']  # тип контакта
                                        )
        ContactsInfo.save(new_contact_info)
        return HttpResponse("OK")
