# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('rater_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('time_stamp', models.DateField()),
                ('movie_id', models.ForeignKey(to='ratings.Movies')),
                ('rater_id', models.ForeignKey(to='ratings.Rater')),
            ],
        ),
    ]
