# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20150630_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='id',
        ),
        migrations.AddField(
            model_name='rater',
            name='age',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.CharField(default=None, max_length=6),
        ),
        migrations.AddField(
            model_name='rater',
            name='job',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='rater',
            name='zipcode',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='rater',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='time_stamp',
            field=models.BigIntegerField(default=0),
        ),
    ]
