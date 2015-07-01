# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0008_auto_20150701_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='zipcode',
            field=models.CharField(max_length=20),
        ),
    ]
