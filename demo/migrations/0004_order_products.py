# Generated by Django 4.2.4 on 2023-08-22 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_remove_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', through='demo.OrderPosition', to='demo.product'),
        ),
    ]