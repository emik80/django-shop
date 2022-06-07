from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Contact


class ContactForm(ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Ваше ім'я"}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Ваш email'}))
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Тема'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Текст повідомлення'}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

