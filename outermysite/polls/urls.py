from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^search/', views.searchMovie, name = 'searchMovie'),
        url(r'^exact/',views.exactMovie, name = 'exactMovie'),
        ]
