# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-03 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0014_auto_20170822_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('userSender', models.CharField(max_length=100)),
                ('userReciever', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]