# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-24 02:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0003_auto_20180424_0233'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OfficeLocation',
            new_name='Office',
        ),
    ]
