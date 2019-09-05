# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-02 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0049_auto_20190826_1837'),
        ('journal', '0034_remove_issue_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='articles',
            field=models.ManyToManyField(blank=True, null=True, related_name='issues', to='submission.TransArticle'),
        ),
    ]
