# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from ratings.models import Rater, Movie, Rating
import pandas as pd

def load_movie_data(apps, schema_editor):
    movie_df = pd.read_csv('fixtures/movies.csv', names=["movie_id", "title", "genre"])
    movie_df.fillna(' ', inplace=True)

    for row in movie_df.iterrows():
        movie_obj = row[1]
        movie_instance = Movie.objects.create(movie_id=movie_obj.movie_id, title=movie_obj.title, genre=movie_obj.genre)
        movie_instance.save()


def load_rater_data(apps, schema_editor):
    rater_df = pd.read_csv('fixtures/users.csv', names=["rater_id", "gender", "age", "job", "zipcode"])
    rater_df.fillna(' ', inplace=True)

    for row in rater_df.iterrows():
        rater_obj = row[1]
        rater_instance = Rater.objects.create(
            rater_id=rater_obj.rater_id,
            gender=rater_obj.gender,
            age=rater_obj.age,
            job=rater_obj.job,
            zipcode=rater_obj.zipcode
        )
        rater_instance.save()


def load_rating_data(apps, schema_editor):
    rating_df = pd.read_csv('fixtures/ratings.csv', names=["rater_id", "movie_id", "rating", "time_stamp"])
    rating_df.fillna(' ', inplace=True)

    for row in rating_df.iterrows():
        rating_obj = row[1]
        rating_instance = Rating.objects.create(rating=rating_obj.rating, time_stamp=rating_obj.time_stamp)
        if rating_obj.rater_id:
            rater_id = Rater.objects.get(rater=rating_obj.rater_id)
            rating_instance.rater_id = rater_id
            rating_instance.save()
        if rating_obj.movie_id:
            movie_id = Movie.objects.get(movie=rating_obj.movie_id)
            rating_instance.movie_id = movie_id
            rating_instance.save()





class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20150630_1736'),
    ]

    operations = [
        migrations.RunPython(load_movie_data),
        migrations.RunPython(load_rater_data),
        migrations.RunPython(load_rating_data)

    ]
