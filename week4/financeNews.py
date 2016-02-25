import requests
import re
from bs4 import BeautifulSoup

#using the requests library, we retrieve documents from a site
page = requests.get("http://www.barrick.com/investors/news/default.aspx").content

#beautifulsoup is a great library for parsing web data.
#creating a page variable

soup = BeautifulSoup(page, "html.parser")

#retrieve the news headlines from Barrick Gold
def getHeadlines():
    rawHeadlines = soup.find_all("span",{"class":"ModuleHeadline"})
    headlines = []
    
    for headline in rawHeadlines:
        headline = headline.string
        #problem: we get investors > news as one of the headlines
        #use regex
        '''match = re.search(r'>', headline)
        if match:
            break
        else:
            headlines.append(headline)'''
        headlines.append(headline)

    return headlines

#get the headlines and print them. You can instead use the function above for general processing
#this will work nicely with the regex fix
headlines = getHeadlines()
for x in headlines:
    print x
    
