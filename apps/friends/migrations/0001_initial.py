# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-30 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='friends',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accept', to='friends.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='friends.User'),
        ),
    ]
