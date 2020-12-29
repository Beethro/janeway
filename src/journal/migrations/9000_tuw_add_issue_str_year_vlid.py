# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-29 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0040_auto_20200805_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='tuw_issue_str',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='tuw_vlid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='tuw_year',
            field=models.IntegerField(null=True),
        ),
    ]