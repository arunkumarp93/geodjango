# Generated by Django 3.2.5 on 2021-07-16 13:38

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(message='Maximum 16 digits allowed without space and any special character except + sign ', regex='^\\+?1?\\d{8,15}$')])),
                ('language', models.CharField(max_length=20)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polygon_name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('polygon', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.providers')),
            ],
        ),
    ]
