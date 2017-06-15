import csv
with open('ZT_lookup.csv','rb') as file:
	ct = 0
	reade = csv.reader(file,delimiter = ';')
	for row in reade:
		if row[0] != "None" and  row[0] != "url":
			ct += 1
	print ct
		
