from django.urls import path

from .views import *

urlpatterns = [
    path('add_equipment/', add_equipment, name='add_equipment'),

    ]
