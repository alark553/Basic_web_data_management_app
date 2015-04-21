# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device_range',
            name='device',
        ),
        migrations.DeleteModel(
            name='Device_Range',
        ),
        migrations.AddField(
            model_name='device',
            name='device_range',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
