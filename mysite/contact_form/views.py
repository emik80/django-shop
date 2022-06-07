from django.shortcuts import render
from django.views.generic import CreateView

from mysite import post_settings
from .models import Contact
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm


class ContactCreate(CreateView):
    model = Contact
    template_name = 'contact_form/contact_form.html'
    success_url = reverse_lazy('contact_form:success_page')
    form_class = ContactForm

    def form_valid(self, form):
        # Creating a message to send
        data = form.data
        subject = f"Повідомлення з форми від {data['name']} email: {data['email']} Тема: {data['subject']}"
        email(subject, data['message'])
        return super().form_valid(form)


# Message sending function
def email(subject, content):
    send_mail(subject=subject,
              message=content,
              from_email=post_settings.EMAIL_HOST_USER,
              recipient_list=post_settings.RECIPIENT_LIST
              )


# Reporting the successful completion of a form
def success(request):
    return render(request, 'contact_form/success.html')
