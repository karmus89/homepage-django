# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('content', markdownx.models.MarkdownxField()),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
