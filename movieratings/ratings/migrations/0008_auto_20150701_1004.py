# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from ratings.models import Movie
import pandas as pd

def load_movie_data(apps, schema_editor):
    movie_df = pd.read_csv('ratings/fixtures/movies.csv', names=["movie_id", "title", "genre"])
    for row in movie_df.iterrows():
        movie_obj = row[1]
        Movie.objects.create(movie=movie_obj.movie_id, title=movie_obj.title, genre=movie_obj.genre)

class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0007_auto_20150701_1003'),
    ]

    operations = [
        migrations.RunPython(load_movie_data),
    ]
