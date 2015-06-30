from django.db import models

# Create your models here.

class Rater(models.Model):
    #id = models.Field.db_column
    rater = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=6, default=None)
    age = models.IntegerField(default=None)
    job = models.CharField(max_length=200, default=None)
    zipcode = models.IntegerField(default=None)





class Movie(models.Model):
    movie = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(default=0)
    time_stamp = models.BigIntegerField(default=0)

