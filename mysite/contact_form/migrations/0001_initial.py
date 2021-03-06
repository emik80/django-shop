# Generated by Django 3.2.13 on 2022-06-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Ім'я")),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('subject', models.TextField(max_length=200, verbose_name='Тема')),
                ('message', models.TextField(max_length=1000, verbose_name='Повідомлення')),
                ('completed', models.BooleanField(default=False, verbose_name='Вирішено')),
            ],
            options={
                'verbose_name': 'Звернення',
                'verbose_name_plural': 'Звернення',
            },
        ),
    ]
