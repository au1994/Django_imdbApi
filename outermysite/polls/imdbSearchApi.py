import requests
import sys
import traceback
from bs4 import BeautifulSoup

def getSearchResults(movie):
    
    url = "http://www.imdb.com/find?s=tt&q="+movie
    
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit("Slow internet connection")
    
    soup = BeautifulSoup(r.content, "html.parser")
    movies = soup.find_all("td", {"class":"result_text"})
    
    jsonArray = [] 
    
    if len(movies)==0:
        jsonObject={}
        jsonObject['Error']="No results found"
        return jsonObject
    
    for item in movies:
        if not(item == None):
            title = item.get_text().strip()
            url = item.find("a").get("href")
            Id = url[7:16]
        url = "http://www.imdb.com"+url
        jsonObject={}
        jsonObject['Title']=title
        jsonObject['Url']=url
        jsonObject['Id']=Id
        jsonArray.append(jsonObject)
    
    return jsonArray
