# Generated by Django 4.0.5 on 2023-08-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlcf_online', '0002_alter_info_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='comment',
            field=models.CharField(default='none', max_length=400),
            preserve_default=False,
        ),
    ]
