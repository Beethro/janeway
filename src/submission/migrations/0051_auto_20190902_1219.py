# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-02 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0050_auto_20190902_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldanswer',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.TransArticle'),
        ),
    ]
