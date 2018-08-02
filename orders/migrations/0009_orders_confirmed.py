# Generated by Django 2.0.7 on 2018-08-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orders_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders_Confirmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('order_items', models.CharField(max_length=1024)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('topping', models.IntegerField()),
                ('toppings', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]