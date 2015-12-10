#user/local/bin/python
#uses python3
import sys, os, csv, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inflation.settings") 
from datetime import datetime
from django.conf import settings
from reports.models import Interest

reader = csv.reader(open("scripts/interestRate.csv", "rU"), dialect=csv.excel)
cleanedRate = []
cleanedDate = []
for row in reader:
  #da[0] = eval(da[0])
  if row[0][0] == '1' and row[0][1] == '/':
    date = datetime.strptime(row[0], "%m/%d/%Y")
    cleanDated = "{0}-{1}-{2}".format(date.year, date.month, date.day)
    print(cleanDated)
    cleanedDate.append(cleanDated)
    cleanedRate.append(float(row[1]))
    
#cleaned.pop(0)
print(cleanedRate)
print(cleanedDate)
length = len(cleanedRate)
for i in range(length):
  b, bcreated = Interest.objects.get_or_create(rate=cleanedRate[i], date=cleanedDate[i])
  print(b)