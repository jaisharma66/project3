# Generated by Django 2.0.7 on 2018-08-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20180802_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='topping',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]