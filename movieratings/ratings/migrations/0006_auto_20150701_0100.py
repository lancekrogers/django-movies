# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0005_auto_20150701_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='time_stamp',
        ),
        migrations.AddField(
            model_name='movie',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False, auto_created=True, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rater',
            name='job',
            field=models.IntegerField(),
        ),
    ]
