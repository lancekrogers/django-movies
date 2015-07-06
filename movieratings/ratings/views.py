from django.shortcuts import render, render_to_response as rtr
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.http import HttpResponse
from django.template import RequestContext

from ratings.models import Movie, AvgMovRating, Rating, Rater

# Create your views here.



def movie_page(request, movie_id):
    try:
        movie = Movie.objects.get(movie=movie_id)
        title = movie.title
        movie_title = title.replace(' ', '')
    except Movie.DoesNotExist:
        raise Http404
    return render(request, 'ratings/movie_page.html', {'movie_id': movie_id, 'movie_title': movie_title})


def all_movies(request):
    return HttpResponse("I am a place where all the movies hang out")


def rater_page(request, rater_id):
    return HttpResponse("I am a an individual, I am also a rater.")


def all_raters(request):
    return HttpResponse("I am a place where all the raters hang out")


def top_twenty_ratings(request):

    top_list = AvgMovRating.objects.order_by('avg')[:20]
    x = 10
    return HttpResponse('top twenty movies go here')
