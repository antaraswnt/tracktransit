# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_number', models.CharField(max_length=10)),
                ('source', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('route_polyline', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=10)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Route')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleStatus',
            fields=[
                ('vehicle_id', models.IntegerField(primary_key=True, serialize=False)),
                ('route_number', models.CharField(max_length=10)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('updated_at', models.DateTimeField()),
                ('status', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='vehicleroute',
            unique_together=set([('vehicle', 'route')]),
        ),
    ]
