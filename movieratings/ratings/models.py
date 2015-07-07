from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rater(models.Model):
    user = models.OneToOneField(User, null=True)
    rater = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    job = models.IntegerField()
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return '{}-{}-{}-{}'.format(self.rater, self.gender, self.age, self.job)

    def movies_rated(self):
        return Rating.objects.filter(rater=self)



class Movie(models.Model):
    movie = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    
    def __str__(self):
        return '{}'.format(self.title)

    def rated_by(self):
        return Rating.objects.filter(movie=self)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(default=0)
    time_stamp = models.BigIntegerField()

    def __str__(self):
        return '{}-{}-{}'.format(self.rater, self.movie.title, self.rating)


class AvgMovRating(models.Model):
    movie = models.ForeignKey(Movie)
    avg = models.FloatField()

    def __str__(self):
        return '{}-{}'.format(self.movie, self.avg)

