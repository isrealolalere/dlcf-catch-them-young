# Generated by Django 4.0.5 on 2023-08-16 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlcf_online', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='phone_no',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be exactly 10 digits without spaces or dashes.', regex='^\\d{17}$')]),
        ),
    ]