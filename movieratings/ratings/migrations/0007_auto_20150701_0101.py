# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from ratings.models import Movie, Rater, Rating
import pandas as pd

def load_movie_data(apps, schema_editor):
    movie_df = pd.read_csv('ratings/fixtures/movies.csv', names=["id", "title", "genre"])
    for row in movie_df.iterrows():
        movie_obj = row[1]
        Movie.objects.create(id=movie_obj.id, title=movie_obj.title, genre=movie_obj.genre)


def load_rater_data(apps, schema_editor):
    rater_df = pd.read_csv('ratings/fixtures/users.csv', names=["id", "gender", "age", "job", "zipcode"])

    for row in rater_df.iterrows():
        rater_obj = row[1]
        Rater.objects.create(
            id=rater_obj.id,
            gender=rater_obj.gender,
            age=rater_obj.age,
            job=rater_obj.job,
            zipcode=rater_obj.zipcode
        )
    raise Exception()



def load_rating_data(apps, schema_editor):
    rating_df = pd.read_csv('ratings/fixtures/ratings.csv', names=["rater", "movie", "rating"])

    for row in rating_df.iterrows():
        rating_obj = row[1]
        Rating.objects.create(rating=rating_obj.rating)
        if rating_obj.rater:
            rater_id = Rater.objects.get(rater=rating_obj.id)
            Rating.rater_id = rater_id
        if rating_obj.movie:
            movie_id = Movie.objects.get(movie=rating_obj.id)
            Rating.movie_id = movie_id
    raise Exception()




class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0006_auto_20150701_0100'),
    ]

    operations = [
         migrations.RunPython(load_movie_data),
         migrations.RunPython(load_rater_data),
         migrations.RunPython(load_rating_data),
    ]
