#user/local/bin/python
#uses python3
import urllib.request
from bs4 import BeautifulSoup
from reports.models import Unemployment

url = "http://www.bls.gov/cps/cpsaat01.htm" #access the search term through website
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page)
tables = soup.findAll('table') #find all tables
#print(tables)
mainTable = soup.find(id="cps_eeann_year")
#print(mainTable)
for table in tables:
  caption = table.find('caption')
  print(caption)
data = [] #create holder for results
rows = mainTable.findAll('tr')
#print(rows)
for row in rows[1:]:
  dataRow = [] #create smaller list for each row
  for th in row.findAll('th'):
    dataRow.append(th.text)
  for td in row.findAll('td'):
    dataRow.append(td.text) 
  data.append(dataRow)
data.pop()
print(data)
cleanedRate = []
cleanedDate = []
for da in data:
  #da[0] = eval(da[0])
  try:
    if int(da[0]) >= 1947:
      dates = "{}-{}-{}".format(da[0], 1, 1)
      cleanedDate.append(dates)
      cleanedRate.append(eval(da[-2]))
  except ValueError:
    pass
#cleaned.pop(0)
print(cleanedRate)
print(cleanedDate)
length = len(cleanedRate)
for i in range(length):
  b, bcreated = Unemployment.objects.get_or_create(rate=cleanedRate[i], date=cleanedDate[i])
  print(b)