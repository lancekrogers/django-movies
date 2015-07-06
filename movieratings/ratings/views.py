from django.shortcuts import render, render_to_response as rtr
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.http import HttpResponse
from django.template import RequestContext

from ratings.models import Movie, AvgMovRating, Rating, Rater

# Create your views here.


def movie_page(request, movie_id):
    try:
        movie = Movie.objects.get(movie=movie_id)
    except Movie.DoesNotExist:
        raise Http404
    return render(request, 'ratings/movie_page.html', {'movie': movie})


def all_movies(request):
    all_movs = Movie.objects.all()
    return render(request, 'ratings/movie_list.html', {'movies': all_movs})


def rater_page(request, rater_id):
    try:
        rater = Rater.objects.get(rater=rater_id)
    except Movie.DoesNotExist:
        raise Http404
    return render(request, 'ratings/rater.html', {'rater': rater})


def all_raters(request):
    all_rats = Rater.objects.all()
    return render(request, 'ratings/raters-list.html', {'raters': all_rats})


def top_twenty_ratings(request):
    top_list = AvgMovRating.objects.order_by('avg')[:20]
    return render(request, 'ratings/top_twenty.html', {'top_twenty': top_list})
