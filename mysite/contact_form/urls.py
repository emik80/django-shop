from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactCreate.as_view(), name='contact_form'),
    path('success/', success, name='success_page')
]
