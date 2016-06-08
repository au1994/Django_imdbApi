import json
import pdb
import sys
import traceback

import requests

import imdbScraper

from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def search_movie(request):

    movie = request.GET.get('q', '')
    movie_list = imdbScraper.get_search_results(movie)

    if type(movie_list) is dict:
        if "Service unavailable" in movie_list.values():
            status_code = 503
        else:
            status_code = 404
        data = json.dumps(movie_list)
        return HttpResponse(data,
                            content_type='application/json',
                            status=status_code)

    paginator = Paginator(movie_list, 20)
    page = request.GET.get('page')

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(1)

    movies = movies.object_list
    data = json.dumps(movies)

    return HttpResponse(data,
                        content_type='application/json',
                        status=200)


def exact_movie(request, movie_id):

    data = imdbScraper.get_movie_results(movie_id)
    if 'error' in data:
        if "Service unavailable" in data.values():
            status_code = 503
        else:
            status_code = 404
    else:
        status_code = 200
    data = json.dumps(data)
    return HttpResponse(data,
                        content_type='application/json',
                        status=status_code)
