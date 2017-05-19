from lxml import html
from bs4 import BeautifulSoup
import requests
import urllib2
__author__ = 'Nicholas Hernandez'
def getProfessorRating(input):
    ratingSite = requests.get('http://www.ratemyprofessors.com/'+input)
    ratingPage = html.fromstring(ratingSite.content)
    rating = ratingPage.xpath(('//div[@class = "grade"]/text()'))
    tempstr = str(rating)[str(rating).find("'")+1:]
    returnString = tempstr[:tempstr.find("'")]
    return returnString

def getSJSUProfessorList():
    sjsu = requests.get('http://www.sjsu.edu/cs/community/faculty/')
    htmlTree = html.fromstring(sjsu.content)
    profList = htmlTree.xpath(('//table//a["content"]/text()'))
    return profList

def findOnRMP():
    profUrl = "http://www.ratemyprofessors.com/search.jsp?query="+ professor.replace(" ","+", 1)
    ratemyprof = requests.get(profUrl)
    profTree = html.fromstring(ratemyprof.content)
    schools = profTree.xpath(('//span[@class = "sub"]/text()'))
    return schools

professorList = getSJSUProfessorList()
for professor in professorsList:
    #print professor
    schools = findOnRMP()
    index = 0
    found = False
    for school in schools:
        if school == "San Jose State University, Computer Science":
            found = True
            break
        index = index+1

    if found == False:
        print "none"
        continue;

    professorPage = urllib2.urlopen(profUrl)
    theSoup = BeautifulSoup(professorPage,"lxml")

    if index ==0:
        Links = theSoup.find("li", attrs= {"class" : "listing PROFESSOR"})
    else:
        Links = theSoup.find("li", attrs= {"class" : "listing PROFESSOR"}).find_next_siblings()


    for link in Links:
        strng = str(link)
        if strng.find("San Jose State")>=0:
            tempstr = strng[strng.find("href"):]
            tempstr = tempstr[tempstr.find('"')+1:]
            tempstr = tempstr[:tempstr.find('"')]
            print(getProfessorRating(tempstr))




