# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-04 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0049_auto_20201117_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]