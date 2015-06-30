from django.db import models

# Create your models here.

class Rater(models.Model):
    #id = models.Field.db_column
    rater_id = models.IntegerField()


class Movies(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)


class Ratings(models.Model):
    rater_id = models.ForeignKey(Rater)
    movie_id = models.ForeignKey(Movies)
    rating = models.IntegerField(default=0)
    time_stamp = models.DateField()

