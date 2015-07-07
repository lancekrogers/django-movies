from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response as rtr, render_to_response
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.http import HttpResponse
from django.template import RequestContext
from ratings.forms import RatingForm
from django.core.urlresolvers import reverse
from ratings.models import Movie, AvgMovRating, Rating, Rater
from django.contrib.auth.decorators import login_required
# Create your views here.


def movie_page(request, movie_id):
    try:
        movie = Movie.objects.get(movie=movie_id)
        try:
            avg_rat = AvgMovRating.objects.filter(movie=movie.movie)
            for mov in avg_rat:
                rating = mov.avg
                if rating == 0.0:
                    a_rat = 'Has no average rating'
                else:
                    a_rat = rating
        except:
            pass
    except Movie.DoesNotExist:
        raise Http404
    return render(request, 'ratings/movie_page.html', {'movie': movie, 'avg': a_rat})


def all_movies(request):
    all_movs = Movie.objects.all()
    context = {'movies': all_movs}
    return render(request, 'ratings/movie_list.html', context)


def rater_page(request, rater_id):
    try:
        rater = Rater.objects.get(rater=rater_id)
        rated_mov = Rater.movies_rated(rater)
    except Movie.DoesNotExist:
        raise Http404
    context = {'rater': rater, 'rated_movies': rated_mov}
    if request.user == rater.user:
        if request.POST:
            rate_instance = Rating(rater=rater)
            form = RatingForm(request.POST, instance=rate_instance)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse("best_movies"))

        form = RatingForm()
        context['form'] = form
    return render_to_response('ratings/rater.html', context, context_instance=RequestContext(request))


def all_raters(request):
    all_rats = Rater.objects.all()
    return render(request, 'ratings/raters-list.html', {'raters': all_rats})


def top_twenty_ratings(request):
    top_list = AvgMovRating.objects.order_by('-avg')[:20]
    return render(request, 'ratings/top_twenty.html', {'top_twenty': top_list})


def user_registration(request):
    if request.POST:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_form = UserCreationForm({
            'username': username,
            'password1': password1,
            'password2': password2
        })
        try:
            user_form.save(commit=True)
            return HttpResponseRedirect("/")
        except ValueError:
            return render_to_response("registration/create_user.html",
                                      {'form': user_form},
                                      context_instance=RequestContext(request))

    return render_to_response("registration/create_user.html",
                              {'form': UserCreationForm()},
                              context_instance=RequestContext(request))


