# Generated by Django 4.1 on 2022-09-25 15:02

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('volume', models.IntegerField(null=True)),
                ('urlsImage', models.ImageField(upload_to=api.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('urlsImage', models.ImageField(upload_to=api.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(null=True)),
                ('price', models.TextField(null=True)),
                ('volume', models.IntegerField(null=True)),
                ('urlsImage', models.ImageField(upload_to=api.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.TextField(null=True)),
                ('userPassword', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userToken', models.TextField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('coffee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.coffee')),
                ('dessert', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.dessert')),
                ('topping', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.topping')),
            ],
        ),
    ]
