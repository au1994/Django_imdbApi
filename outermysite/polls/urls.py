from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^search/', views.search_movie, name='search_movie'),
        url(r'^get/([a-z0-9A-Z]+)/', views.exact_movie),
        ]
