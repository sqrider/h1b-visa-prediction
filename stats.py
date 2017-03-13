import csv
import random

csv_file = open("h1b.csv") 
header = csv_file.readline() # remove header

newFile = open("subset_h1b.csv", 'w')
lines = list(csv.reader(csv_file, delimiter=','))

subset = []
status_map = {}
year_map = {}
year_certified = {}
for l in lines:
  status_map[l[0]] = status_map.get(l[0], 0) + 1
  year_map[l[6]] = year_map.get(l[6], 0) + 1
  if l[0] == 'CERTIFIED':
  	year_certified[l[6]] = year_certified.get(l[6], 0) + 1
  subset.append(l)

for k,v in status_map.items():
  print k + ": " + str(v)

for k,v in year_map.items():
  print k + ": " + str(v)

for k,v in year_certified.items():
  print k + ": " + str(float(v)/float(year_map[k]))

# Take a random sub sample of 50,000
random.shuffle(subset)
writer = csv.writer(newFile, delimiter=',')
certified = 0
non_certified = 0
for f in subset[:50000]:
  if f[0] == 'CERTIFIED':
  	certified += 1
  else:
  	non_certified += 1
  writer.writerow(f)

total = certified + non_certified
print "percentage certified: " + str(float(certified)/float(total))