# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-20 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0045_auto_20190820_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleauthororder',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.TransArticle'),
        ),
    ]
