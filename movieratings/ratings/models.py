from django.db import models

# Create your models here.

class Rater(models.Model):
    #id = models.Field.db_column
    rater = models.IntegerField()


class Movie(models.Model):
    movie = models.IntegerField()
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(default=0)
    time_stamp = models.DateField()

