from django.contrib import admin
from .models import Movie, Rater, Rating, AvgMovRating
# Register your models here.

admin.site.register(Movie)
admin.site.register(Rater)
admin.site.register(Rating)
admin.site.register(AvgMovRating)