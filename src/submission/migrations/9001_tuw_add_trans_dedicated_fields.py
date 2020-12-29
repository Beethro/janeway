# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-03 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '9000_tuw_add_visible_to_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='abstract_de',
            field=models.TextField(blank=True, help_text='Abstract (de)', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='subtitle_de',
            field=models.CharField(blank=True, help_text='Subtitle of the article display format; Title: Subtitle (de)', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_de',
            field=models.CharField(blank=True, help_text='Your article title (de)', max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='KeywordDe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='keywords_de',
            field=models.ManyToManyField(blank=True, null=True, to='submission.KeywordDe'),
        ),
    ]