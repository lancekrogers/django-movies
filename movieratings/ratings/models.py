from django.db import models

# Create your models here.

class Rater(models.Model):
    rater = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    job = models.IntegerField()
    zipcode = models.IntegerField()


class Movie(models.Model):
    movie = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(default=0)

