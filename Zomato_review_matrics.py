import json
import glob
import sys
import csv
import os
from datetime import datetime
from datetime import date

# input_dir = sys.argv[1]
output_file = sys.argv[1]
option = sys.argv[2]
output_stats = [['min','max','avg']]

for file_name in glob.glob("*.json"):
	try:
		print 'processing '+file_name
		if os.path.getsize(file_name) > 0:
			with open(file_name) as json_data:
				reviews = json.load(json_data)
				if reviews and len(reviews)>0:
					dates_hash = {}
					found = False
					for review in reviews['reviews']:
						if review['date'] and len(review['date'])>0:
							found = True
							# print 'First if'
							#find daily stats
							if option=="day":
								# print 'Day found'
								if not review['date'] in dates_hash:
									# print 'Hash found'
								# .has_key(review['date']):
									dates_hash[review['date']] = 1
								else:
									dates_hash[review['date']] +=1
							elif option=="week":
								#find weekly stats
								review_date_list = review['date'].split('-')
								date_num = date(int(review_date_list[0]),int(review_date_list[1]),int(review_date_list[2])).isocalendar()
								year_week = str(date_num[0])+'_'+str(date_num[1])
								
								if not year_week in dates_hash:
									dates_hash[year_week] = 1
								else:
									dates_hash[year_week] += 1	
							elif option=="month":
								#find monthly stats
								date_year = review['date'].split('-')
								year_month = str(date_year[0])+'_'+str(date_year[1])
								# date_obj = datetime.strptime(review['date'],'%d %B %Y')
								# year_month = date_obj.strftime('%Y')+'_'+date_obj.strftime('%m')
								if not year_month in dates_hash:
									# print dates_hash['year_month'], 'New one'
									dates_hash[year_month] = 1
								else:
									# print dates_hash[year_month]
									dates_hash[year_month] += 1
					if found:
						#print dates_hash
						counts = dates_hash.values()
						avg = (float(sum(counts))/float(len(counts)))
						print avg
						output_stats.append([min(counts),max(counts),avg])
	except Exception, e:
        	print 'Handled exception: '+str(e)
with open(output_file, 'w') as myfile:
	wr = csv.writer(myfile, delimiter=',')#, quoting=csv.QUOTE_ALL)
	wr.writerows(output_stats)
print 'Writtng stats to : ' +output_file
