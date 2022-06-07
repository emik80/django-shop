from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Ім`я"}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Прізвище"}))
    address = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Адреса"}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Місто"}))
    postal_code = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Індекс"}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'city', 'postal_code']
