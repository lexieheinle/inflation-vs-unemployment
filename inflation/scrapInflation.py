#user/local/bin/python
#uses python3
import sys, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inflation.settings") 
import urllib.request
from bs4 import BeautifulSoup
from reports.models import Inflation
    
url = "http://www.usinflationcalculator.com/inflation/historical-inflation-rates/" 
page = urllib.request.urlopen(url).read()

soup = BeautifulSoup(page, "html.parser")

data = []
for tr in soup.find_all('tr')[1:]:
    dataRow = []
    for header in tr.find_all('th'):
        tds = tr.find_all('td')
        dataRow.append(header.text)
        dataRow.append(tds[0].text)
    data.append(dataRow)
cleanedRate = []
cleanedDate = []
for da in data:
    try:
        if int(da[0]) >= 1947:
            dates = "{0}-{1}-{2}".format(da[0], 1, 1)
            cleanedDate.append(dates)
            cleanedRate.append(float(da[1]))
    except IndexError as e:
        print("Error: Index of Zero. Still works, though\nDetails: {0}".format(e))
            
length = len(cleanedRate)
for i in range(length):
    b, bcreated = Inflation.objects.get_or_create(rate=cleanedRate[i], date=cleanedDate[i])
    print(b) 
     