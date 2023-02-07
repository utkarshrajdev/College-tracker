from .models import College,City,State

import requests
from bs4 import BeautifulSoup



def career(): 
    print('df')

    URL = "https://www.careers360.com/colleges/india-colleges-fctp"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    
    collegetitles = soup.find_all('h3',class_="college_name")
    citystate = soup.find_all('div',class_="content_block d-none d-md-block d-md-flex flex-row justify-content-between")
    # print(citystate)
    global colleges, cities, states
    colleges = []
    cities = []
    states = []

    for detail in citystate:
        detail = detail.find_all('span')
        detail = detail[0]
        detail = detail.get_text()
        detail = detail.split(", ")
        city = detail[0]
        city = city.lstrip()
        state = detail[1]
        state = state.rstrip()
        # state = state.split(" ")
        # state = state[0]
        cities.append(city)
        states.append(state)
    for title in collegetitles:
        title = title.find('a')
        title = title.get_text()
        colleges.append(title)
    
    
    print(cities)
    print(states)
    print(colleges)
        
    

    


    

def savestate() :
    career()
    statelist = [*set(states)]
    for i in range(len(statelist)) :
        statename = statelist[i]
        if State.objects.all().filter(state=statename).exists() == False :
            ins = State(state=statename)
            ins.save()

def savecity() :
    career()
    citylist = []

    statelist = []
    for i in range(len(cities)):
        if cities[i] not in citylist:
            citylist.append(cities[i])
            statelist.append(states[i])
    for i in range(len(citylist)) :
        cityname = citylist[i] 
        if City.objects.all().filter(city=cityname).exists() == False :
            ins = City(city=cityname, state =State.objects.get(state=statelist[i]))
            ins.save()

def savecollege() :
    career()
    collegelist = []
    for i in range(len(colleges)):
        if colleges[i] not in collegelist:
            collegelist.append(colleges[i])
    for i in range(len(collegelist)) :
        name = collegelist[i]
        if College.objects.all().filter(name=name).exists() == False :
            ins = College(name=name, city=City.objects.get(city=cities[i]))
            ins.save()


def studyguide() :
    import requests
    from bs4 import BeautifulSoup

    URL = "http://www.studyguideindia.com/Colleges/default.asp?Course=B-Tech-Colleges"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    format = soup.prettify

    title=soup.title
    global colleges, cities, states
    colleges = []
    cities = []
    states = []

    images = soup.find_all('img')
    allsrc = []
    for src in images:
        src = src.get('src')
        allsrc.append(src)
        print(src)
