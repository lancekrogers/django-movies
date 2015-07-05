from django.shortcuts import render, render_to_response as rtr
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

from ratings.models import Movie, AvgMovRating, Rating, Rater

# Create your views here.



def movie_page(request, movie_id):
    return HttpResponse("Individual Movie Page")


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
