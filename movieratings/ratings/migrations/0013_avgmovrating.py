# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0012_auto_20150701_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvgMovRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('avg', models.FloatField()),
                ('movie', models.ForeignKey(to='ratings.Movie')),
            ],
        ),
    ]
