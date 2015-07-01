# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0006_auto_20150701_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
