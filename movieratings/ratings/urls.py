from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.top_twenty_ratings, name='best_movies'),
    url(r'^movies/$', views.all_movies, name='all_movies_page'),
    url(r"^movies/(?P<movie_id>[0-9]+)/$", views.movie_page, name='single-movie-page'),
    url(r'^raters/$', views.all_raters, name='rater-hangout'),
    url(r'^raters/(?P<rater_id>[0-9]+)/$', views.rater_page, name='single-rater-page'),

        ]

#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
# ex: /polls/5/results/
#url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
# ex: /polls/5/vote/
#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),