# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-03-15 20:50
from __future__ import unicode_literals

import apps.web.models
import apps.web.storage
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20190314_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='secret_key',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
