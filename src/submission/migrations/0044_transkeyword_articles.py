# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-20 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0043_auto_20190820_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='transkeyword',
            name='articles',
            field=models.ManyToManyField(blank=True, null=True, to='submission.TransArticle'),
        ),
    ]
