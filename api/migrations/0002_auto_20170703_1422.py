# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_content',
            field=models.CharField(max_length=255),
        ),
    ]
