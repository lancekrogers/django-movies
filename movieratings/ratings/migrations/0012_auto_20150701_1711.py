# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from ratings.models import Rating, Rater, Movie

import pandas as pd

def load_rating_data(apps, schema_editor):
    rating_df = pd.read_csv('ratings/fixtures/ratings.csv', names=["rater_id", "movie_id", "rating", 'time_stamp'])


    for row in rating_df.iterrows():
        rating_obj = row[1]
        raters = Rater.objects.get(rater=rating_obj.rater_id)
        movies = Movie.objects.get(movie=rating_obj.movie_id)
        Rating.objects.create(rater=raters, movie=movies, rating=rating_obj.rating, time_stamp=rating_obj.time_stamp)






class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0011_rating_time_stamp'),
    ]

    operations = [
          migrations.RunPython(load_rating_data)
    ]
