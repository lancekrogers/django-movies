# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('time_stamp', models.DateField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='rater_id',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='rater',
            old_name='rater_id',
            new_name='rater',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
        migrations.AddField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(to='ratings.Movie'),
        ),
        migrations.AddField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(to='ratings.Rater'),
        ),
    ]
