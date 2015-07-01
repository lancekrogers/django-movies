# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_auto_20150630_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='rater',
            name='job',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='rater',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
