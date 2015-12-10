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
    data_row = []
    for header in tr.find_all('th'):
        tds = tr.find_all('td')
        data_row.append(header.text)
        data_row.append(tds[0].text)
    data.append(data_row)
cleaned_rate = []
cleaned_date = []
for da in data:
    try:
        if int(da[0]) >= 1947:
            dates = "{0}-{1}-{2}".format(da[0], 1, 1)
            cleaned_date.append(dates)
            cleaned_rate.append(float(da[1]))
    except IndexError as e:
        print("Error: Index of Zero. Still works, though\nDetails: {0}".format(e))
            
length = len(cleaned_rate)
for i in range(length):
    b, bcreated = Inflation.objects.get_or_create(rate=cleaned_rate[i], date=cleaned_date[i])
    print(b) 
     