#user/local/bin/python
#uses python3
import sys, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inflation.settings") 
import urllib.request
from bs4 import BeautifulSoup
from reports.models import Inflation
    
import urllib, urllib2, string, datetime, time, re
from django.template.defaultfilters import slugify, urlize

url = "http://www.usinflationcalculator.com/inflation/historical-inflation-rates/" 
page = urllib.request.urlopen(url).read()

soup = BeautifulSoup(page, "html.parser")

data = []
for tr in soup.find_all('tr')[1:]:
    dataRow = []
    for header in tr.find_all('th'):
        tds = tr.find_all('td')
        dataRow.append(header.text)
        dataRow.append(td[0].text)
    data.append(dataRow)
print (data)
    
        
