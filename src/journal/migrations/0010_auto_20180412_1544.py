# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-12 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_merge_20180208_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleordering',
            options={'ordering': ('order', 'section')},
        ),
        migrations.AlterModelOptions(
            name='bannedips',
            options={'verbose_name_plural': 'Banned IPs'},
        ),
        migrations.AlterModelOptions(
            name='sectionordering',
            options={'ordering': ('order', 'section')},
        ),
    ]
