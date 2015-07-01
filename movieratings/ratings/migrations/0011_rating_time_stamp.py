# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0010_auto_20150701_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='time_stamp',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
