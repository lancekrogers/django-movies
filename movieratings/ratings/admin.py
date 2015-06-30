from django.contrib import admin
from .models import Movies, Rater, Ratings
# Register your models here.

admin.site.register(Movies)
admin.site.register(Rater)
admin.site.register(Ratings)
