# Generated by Django 5.0.7 on 2024-07-28 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0003_car_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('date_rent_beg', models.DateTimeField()),
                ('date_rent_fin', models.DateTimeField()),
                ('car_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent_app.car')),
            ],
        ),
    ]
