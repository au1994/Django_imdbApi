import requests
import sys
import traceback
from bs4 import BeautifulSoup

def getMovieResults(Id):
    
    url = "http://www.imdb.com/title/"+Id+"/?ref_=fn_al_tt_1"
    
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        print "Unable to connect"
        raise SystemExit("Slow internet connection")
    
    soup = BeautifulSoup(r.content, "html.parser")
    
    movieDetails = soup.find("div", {"class" : "plot_summary"})
    
    jsonArray = []
    
    if movieDetails==None:
        print "No results found"
        jsonObject={}
        jsonObject['Error']="No results found"
        return jsonObject
    
    description = movieDetails.find("div", {"class" : "summary_text"})
    
    director = movieDetails.find_all("span", {"itemprop" : "director"})
    
    writer = movieDetails.find_all("span", {"itemprop" : "creator"})
    
    actor = movieDetails.find_all("span", {"itemprop" : "actors"})
    
    rating = soup.find("span", {"itemprop" : "ratingValue"})
    
    titleDetails = soup.find("div", {"class" : "title_wrapper"})
    
    title = titleDetails.find("h1", {"itemprop" : "name"})
    
    duration = titleDetails.find("time", {"itemprop" : "duration"})
    
    releaseDate = titleDetails.find(
            "meta",
            {"itemprop" : "datePublished"}
            )
    
    genre = titleDetails.find_all("span", {"itemprop" : "genre"})
    
    jsonObject = {}
    
    if not(title == None):
        jsonObject['Title'] = title.get_text().strip()
    
    if not(duration == None):
        jsonObject['Duration'] = duration.get_text().strip()
    
    if not(releaseDate == None):
        jsonObject['ReleaseDate'] = releaseDate['content']
    
    if not(description == None):
        jsonObject['Description'] = description.get_text().strip()
    
    if not(director == None):
        directors=""
        for item in director:
            directors = directors + item.get_text().strip() + ", "
        jsonObject['Directors'] = directors
    
    if not(genre == None):
        genres=""
        for item in genre:
            genres = genres + item.get_text().strip() + " "
        jsonObject['Genre']=genres
    
    if not(writer == None):
        writers=""
        for item in writer:
            writers = writers + item.get_text().strip() + " "
        jsonObject['Writer'] = writers
    
    if not(actor == None):
        actors=""
        for item in actor:
            actors = actors + item.get_text().strip() + " "
        jsonObject['Actors'] = actors
    
    if not(rating == None):
        jsonObject['Rating'] = rating.get_text().strip()
    
    return jsonObject
