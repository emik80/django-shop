from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ім'я")
    email = models.EmailField(max_length=200, verbose_name='Email')
    subject = models.TextField(max_length=200, verbose_name='Тема')
    message = models.TextField(max_length=1000, verbose_name='Повідомлення')
    completed = models.BooleanField(default=False, verbose_name='Вирішено')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Звернення'
        verbose_name_plural = 'Звернення'
