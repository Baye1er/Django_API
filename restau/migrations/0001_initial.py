# Generated by Django 4.0.2 on 2022-05-21 21:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restau_name', models.CharField(max_length=200)),
                ('street', models.CharField(blank=True, max_length=400)),
                ('city', models.CharField(blank=True, max_length=400)),
                ('zip_code', models.IntegerField(default=0)),
                ('website', models.URLField(blank=True, max_length=420)),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\221?\\d{9,10}$')])),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
