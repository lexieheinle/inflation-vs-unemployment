#user/local/bin/python
#uses python3
import sys, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inflation.settings") 
import urllib.request
from bs4 import BeautifulSoup
from reports.models import Unemployment

url = "http://www.bls.gov/cps/cpsaat01.htm" #access the search term through website
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page)
tables = soup.findAll('table') #find all tables
#print(tables)
main_table = soup.find(id="cps_eeann_year")
#print(mainTable)
for table in tables:
  caption = table.find('caption')
  print(caption)
data = [] #create holder for results
rows = main_table.findAll('tr')
#print(rows)
for row in rows[1:]:
  data_row = [] #create smaller list for each row
  for th in row.findAll('th'):
    data_row.append(th.text)
  for td in row.findAll('td'):
    data_row.append(td.text) 
  data.append(data_row)
data.pop()
print(data)
cleaned_rate = []
cleaned_date = []
for da in data:
    try:
        if int(da[0]) >= 1947:
          dates = "{0}-{1}-{2}".format(da[0], 1, 1)
          cleaned_date.append(dates)
          cleaned_rate.append(float(da[-2]))
    except ValueError as e:
        print("Error: Value error. Still works, though\nDetails: {0}".format(e))

#cleaned.pop(0)
print(cleaned_rate)
print(cleaned_date)
length = len(cleaned_rate)
for i in range(length):
  b, bcreated = Unemployment.objects.get_or_create(rate=cleaned_rate[i], date=cleaned_date[i])
  print(b)