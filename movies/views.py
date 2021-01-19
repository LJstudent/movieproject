
from django.shortcuts import render

from .models import Movies


def index(request):
    latest_movies_list = Movies.objects.order_by('-pub_date')[:5]
    context = {'latest_movies_list': latest_movies_list}
    return render(request, 'movies/index.html', context)