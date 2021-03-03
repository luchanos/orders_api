from django.urls import path
from .views import *


urlpatterns = [
    path('add_equipment_type/', add_equipment_type),
]