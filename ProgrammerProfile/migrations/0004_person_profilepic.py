# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgrammerProfile', '0003_auto_20170328_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='ProfilePic',
            field=models.FileField(default='k', upload_to=b''),
            preserve_default=False,
        ),
    ]