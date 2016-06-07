from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json,requests,sys,traceback
import pdb
import imdbSearchApi
import imdbExactApi

# Create your views here.
def searchMovie(request):

    movie  = request.GET.get('q', '')
    movieList = imdbSearchApi.getSearchResults(movie)

    paginator = Paginator(movieList,20)
    page = request.GET.get('page')

    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(1)

    #print type(movies)
    movies = movies.object_list
    data = json.dumps(movies)
    
    return HttpResponse(data, content_type='application/json')
    

def exactMovie(request):
   
    Id = request.GET.get('q', '')
    data = imdbExactApi.getMovieResults(Id)
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')
