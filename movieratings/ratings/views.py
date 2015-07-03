from django.shortcuts import render, render_to_response
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

from ratings.models import Movie, AvgMovRating, Rating, Rater
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    context = {'title': movies}
    return render_to_response('movie_list.html', context, context_instance=RequestContext(request))

def top_twenty_ratings(request):
    pass


def movie(request, movie_id):
    pass


def rater_page(request):
    pass

