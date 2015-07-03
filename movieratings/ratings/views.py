from django.shortcuts import render, render_to_response as rtr
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

from ratings.models import Movie, AvgMovRating, Rating, Rater
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    context = {'title': movies}
    return rtr('movie_list.html', context)

def top_twenty_ratings(request):
    pass


def movie(request, movie_id):
    pass


def rater_page(request):
    pass

