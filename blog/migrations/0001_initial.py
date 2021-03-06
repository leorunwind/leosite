# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessagePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('pubtime', models.DateTimeField()),
            ],
            options={
                'ordering': ('-pubtime',),
            },
        ),
    ]
