# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='modified_tiem',
            new_name='modified_time',
        ),
    ]
