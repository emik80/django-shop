from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'email', 'completed')
    list_display_links = ('id', 'name', 'subject')
    search_fields = ('email', 'subject', 'message')
    list_editable = ('completed', )
    list_filter = ('completed',)
    pass


admin.site.register(Contact, ContactAdmin)
