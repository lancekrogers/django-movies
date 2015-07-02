# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0012_auto_20150701_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
    ]
