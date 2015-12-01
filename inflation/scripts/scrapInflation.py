from reports.models import Inflation

try:
    from BeautifulSoup import BeautifulSoup
except:
    from bs4 import BeautifulSoup
    
import urllib, urllib2, string, datetime, time, re
from django.template.defaultfilters import slugify, urlize

#html = urllib2.urlopen("http://www.usinflationcalculator.com/inflation/historical-inflation-rates/" )

url = "http://www.usinflationcalculator.com/inflation/historical-inflation-rates/" 
page = urllib.request.urlopen(url).read()

soup = BeautifulSoup(page, "html.parser")

for tr in soup.find_all('tr')[1:]:
     for header in tr.find_all('th'):
      tds = tr.find_all('td')
      print (header.text, tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text, tds[10].text, tds[11].text, tds[12].text) 
