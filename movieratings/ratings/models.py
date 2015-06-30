from django.db import models

# Create your models here.

class Rater(models.model):
    #id = models.Field.db_column
    rater_id = models.IntegerField()


class Movies(models.model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)


class Ratings(models.model):
    rater_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.IntegerField()
    time_stamp = models.DateField()

