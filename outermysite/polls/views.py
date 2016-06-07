from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import requests
import sys
import traceback
import pdb
import imdbScraper


# Create your views here.
def search_movie(request):

    movie = request.GET.get('q', '')
    movie_list = imdbScraper.getSearchResults(movie)

    paginator = Paginator(movie_list, 20)
    page = request.GET.get('page')

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(1)

    # print type(movies)
    movies = movies.object_list
    data = json.dumps(movies)

    return HttpResponse(data, content_type='application/json')


def exact_movie(request):

    Id = request.GET.get('q', '')
    data = imdbScraper.getMovieResults(Id)
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')
