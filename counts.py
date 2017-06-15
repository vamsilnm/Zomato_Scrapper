import csv
import glob
import json
count_list = [['no. of reviews','restaurant_name']]
for filename in glob.glob('*.json'):
	restaurant_name = ''.join((' '.join(filename.split('_')[2:])).split('.')[0])
	with open(filename,'r') as data:
		reviews = json.load(data)
		total_reviews = len(reviews['reviews'])
		count_list.append([total_reviews,restaurant_name]) 
with open('review_count.csv','w') as write_file:
	reviews_count = csv.writer(write_file,delimiter=',')
	reviews_count.writerows(count_list)

