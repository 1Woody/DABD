# Generated by Django 3.0.6 on 2020-05-22 22:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundial_online', '0003_auto_20200522_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilot',
            name='dni',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4', regex='^.{9}$')]),
        ),
    ]
