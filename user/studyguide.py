from .models import College,City,State
import requests
from bs4 import BeautifulSoup

def guide():
    URL = "http://www.studyguideindia.com/Colleges/default.asp?cat=A"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    alltext = []
    alphalinks = []
    numpages = []
    details = []
    allpages = soup.find_all('a',class_='link')

    for tablepage in allpages:
        tablepage = tablepage.get('href')
        alphalinks.append(tablepage)
    alphapages = alphalinks[0:26]

    for alpha in alphapages :
        print('Alphabet - ',alpha)
        URL2 = alpha
        page2 = requests.get(URL2)
        soup2 = BeautifulSoup(page2.content, "html.parser")
        numlinks = soup2.find_all('a',class_='link')
        for tablepage in numlinks:
            tablepage = tablepage.get('href')
            numpages.append(tablepage)
        numpages = numpages[26:]
        for list in numpages :
            m = 1
            n = 2
            print('Number - ',list)
            URL3 = list
            page3 = requests.get(URL3)
            soup3 = BeautifulSoup(page3.content, "html.parser")
            collegetable = soup3.find('table',class_="clg-listing")
            collegelinks = collegetable.find_all('a')
            td = collegetable.find_all('td')
            for title in td :
                title = title.get_text()
                title = title.replace('\n','')
                details.append(title)
            details = details[3:]
            print(details)
            print(len(details))
            print(len(collegelinks))
            for collegeprofile in collegelinks:
                collegeprofile = collegeprofile.get('href')
                URL3 = collegeprofile
                page3 = requests.get(URL3)
                soup3 = BeautifulSoup(page3.content, "html.parser")
                detailtable = soup3.find('table',class_="altcolor1")
                if detailtable != None :
                    td = detailtable.find_all('td')
                    for text in td :
                        text = text.get_text()
                        text = text.replace('\r\n                ','')
                        text = text.replace('\n','')
                        alltext.append(text)
                    temp = ['name','location','state','phone','email','website']
                    temp[1]=details[m]
                    temp[2]=details[n]
                    if 'College Name' in alltext :
                        i = alltext.index("College Name")
                        name = alltext[i+1]
                        temp[0]=name
                    else :
                        temp[0]=('-')
                    if 'Phone' in alltext :
                        i = alltext.index("Phone")
                        phone = alltext[i+1].replace(' ','')
                        temp[3]=phone
                    else :
                        temp[3]='-'
                    
                    if 'E-Mail' in alltext :
                        i = alltext.index("E-Mail")
                        mail = alltext[i+1].replace(' ','')
                        temp[4]=mail
                    else :
                        temp[4]='-'

                    if 'Website' in alltext :
                        i = alltext.index("Website")
                        website = alltext[i+1].replace(' ','')
                        temp[5]=website
                    else :
                        temp[5]='-'
                    print(temp)
                    ins = College(name=temp[0],city=temp[1],state=temp[2],phone=temp[3],email=temp[4],website=temp[5])
                    ins.save()
                temp=[]
                alltext = []
                m = m+3
                n= n+3
            details = []
        numpages = []






        





        


