# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-07 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableau', '0002_auto_20160617_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='personality',
            name='color',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]