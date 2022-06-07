from django.db.models import Count
from .models import *


class DataMixin:
    paginate_by = 9

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()

        context['category'] = None
        context['categories'] = categories

        return context
