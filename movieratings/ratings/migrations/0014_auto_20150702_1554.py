# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from ratings.models import Movie, Rating

from statistics import mean

def populate_avg(apps, schema_editor):
    all_movies = Movie.objects.all()
    for obj in all_movies:
        rat_list = []
        for r in Rating.objects.filter(movie = obj):
            rat_list.append(r.rating)
        try:
            rat = mean(rat_list)
            rating = round(rat, 2)
        except:
            rating = 0
        Movie.objects.create(avg_rating=rating)
        print(Movie.objects.avg_rating)
    raise Exception()




class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0013_movie_avg_rating'),
    ]

    operations = [
        migrations.RunPython(populate_avg)
    ]
