# Generated by Django 4.2.11 on 2024-04-16 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_cart_quantity_furniture_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture_item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
