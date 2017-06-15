import csv
with open ('ZT_urls.csv','w') as newcsvfile:
	writer = csv.writer(newcsvfile)
	with open('ZT_lookup.csv','rb') as csvfile:
	    spamreader = csv.reader(csvfile, delimiter=';',)
	    for row in spamreader:
	    	if row[0] != "None" and  row[0] != "url":
	    		print row[0]
	    		print row[1]	