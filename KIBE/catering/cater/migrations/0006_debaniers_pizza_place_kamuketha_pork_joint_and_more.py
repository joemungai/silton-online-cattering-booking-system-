# Generated by Django 4.1.7 on 2023-03-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cater', '0005_package_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debaniers_Pizza_Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('team_number', models.PositiveIntegerField(default=0)),
                ('charging_per_hour', models.DecimalField(decimal_places=2, max_digits=8)),
                ('phone', models.CharField(max_length=20)),
                ('images', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Kamuketha_pork_joint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('team_number', models.PositiveIntegerField(default=0)),
                ('charging_per_hour', models.DecimalField(decimal_places=2, max_digits=8)),
                ('phone', models.CharField(max_length=20)),
                ('images', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mama_Africa_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('team_number', models.PositiveIntegerField(default=0)),
                ('charging_per_hour', models.DecimalField(decimal_places=2, max_digits=8)),
                ('phone', models.CharField(max_length=20)),
                ('images', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mini_Inn_Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('team_number', models.PositiveIntegerField(default=0)),
                ('charging_per_hour', models.DecimalField(decimal_places=2, max_digits=8)),
                ('phone', models.CharField(max_length=20)),
                ('images', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Panesic_Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('team_number', models.PositiveIntegerField(default=0)),
                ('charging_per_hour', models.DecimalField(decimal_places=2, max_digits=8)),
                ('phone', models.CharField(max_length=20)),
                ('images', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Quivers_Bar_Grill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('team_number', models.PositiveIntegerField(default=0)),
                ('charging_per_hour', models.DecimalField(decimal_places=2, max_digits=8)),
                ('phone', models.CharField(max_length=20)),
                ('images', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]