import urllib
import lxml.html
import urllib2


class Zomato_Lookup():
	def __init__(self,restaurant_name):
		self.restaurant_name = restaurant_name
		self.url = None
		self.RestaurantUrl()
	def RestaurantUrl(self):
		self.restaurant_name = self.restaurant_name.split(' ')
		s = '%20'.join(self.restaurant_name)
		p = 'https://www.zomato.com/php/liveSuggest.php?type=keyword&search_bar=1&q='+s+'&online_ordering=&search_city_id=6&entity_id=6&entity_type=city'
		page = urllib.urlopen(p)#make HTTP request to the site
		doc = lxml.html.document_fromstring(page.read()) # Read the downloaded Page
		k = doc.xpath('/html/body/li/a/@href')
		if len(k) > 0:
			k = k[0]
			rew = k.split('"\"')
			rf = ''.join(rew)
			self.url = rf.replace('\\',"")
		elif len(k) == 0:
			self.url = 'No Match'

			

