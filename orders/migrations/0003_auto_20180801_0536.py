# Generated by Django 2.0.7 on 2018-08-01 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_salads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regular_pizza',
            name='toppings',
        ),
        migrations.RemoveField(
            model_name='sicilian_pizza',
            name='toppings',
        ),
    ]
