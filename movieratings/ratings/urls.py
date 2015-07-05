from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all_movies, name='all-movies-pages'),
    url(r'^(?P<movie.movie>\d+)/movie-page/$', views.movie_page, name='single-movie-page'),
    url(r'^(?P<movie.movie>\d+)/rater-page/$', views.rater_page, name='single-rater-page'),
    url(r'^(?P<movie.movie>\d+)/raters/$', views.all_raters, name='rater-hangout'),
    url(r'^top-movies/$', views.top_twenty_ratings, name='best-movies'),

        ]