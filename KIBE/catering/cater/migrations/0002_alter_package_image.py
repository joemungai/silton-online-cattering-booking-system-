# Generated by Django 4.1.7 on 2023-03-07 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
