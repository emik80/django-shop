from django.urls import path

from . import views
from .views import fondy_callback

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('fondy_callback/', fondy_callback, name='fondy_callback'),
]
