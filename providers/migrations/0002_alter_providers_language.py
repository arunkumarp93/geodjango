# Generated by Django 3.2.5 on 2021-07-16 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providers',
            name='language',
            field=models.CharField(max_length=3),
        ),
    ]
