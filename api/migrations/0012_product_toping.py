# Generated by Django 4.2 on 2023-04-20 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_order_coffee_remove_order_dessert_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='toping',
            field=models.ManyToManyField(to='api.topping'),
        ),
    ]
