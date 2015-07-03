# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from ratings.models import Movie, Rating, AvgMovRating

from statistics import mean



def populate_avg(apps, schema_editor):
    all_movies = Movie.objects.all()
    timer = 0
    for obj in all_movies:
        rat_list = []
        a = '.' * timer
        if timer >= 100:
            timer -= 90
        print('loading...{}'.format(a))
        for r in Rating.objects.filter(movie = obj):
            rat_list.append(r.rating)

        try:
            rating = round(mean(rat_list), 2)
        except:
            rating = 0
        obj.avg_rating = rating
        avg_save = AvgMovRating.objects.create(movie=Movie.objects.get(movie = obj.movie), avg=rating)
        avg_save.save()
        timer += 1
       # print(obj.avg_rating, obj.title)







class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0013_avgmovrating'),
    ]

    operations = [
        migrations.RunPython(populate_avg)
    ]
