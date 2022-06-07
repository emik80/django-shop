from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'email', 'total_cost',
                    'paid', 'payment_id', 'created', 'updated')
    list_editable = ('paid',)
    list_filter = ('user', 'paid', 'updated')
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
