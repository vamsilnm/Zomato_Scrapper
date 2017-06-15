import requests
import json
import urllib
import lxml.html

from zomato_wrapper import Zomato_Wrapper
class ZomatoReviews():
	def __init__(self,url):
		self.url = url
		self.Zomato_Api()
	def Zomato_Api(self):
		page = urllib.urlopen(self.url)
		doc = lxml.html.document_fromstring(page.read())
		tmp = doc.xpath('/html/body/div[@id="mainframe"]/div[@class="wrapper mtop"]/div[@class="row"]/div[@class="res-info-left col-l-11"]/div[@class="ui segment res-header-overlay vr"]/div[@class=""]/div[@class=""]/div[@class="row pos-relative"]/div[@class=" full_obp  col-s-16 clearfix"]/div[@id="progressive_image"]/div[@class="right"]/div[@class="ui left action input res-share-btn"]/div[@id="restaurant-share-shortlink"]/text()')[0].strip()
		url_id = tmp.split('/')[-1]
		locationUrlFromLatLong = "https://developers.zomato.com/api/v2.1/reviews?res_id="+url_id+"&start=0&count=5"
		header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "186d4b03be39f24f4336e165c19d38d1"}
		response = requests.get(locationUrlFromLatLong, headers=header)
		data = response.json()
		data = {i:data[i] for i in data if i=='user_reviews'}
		data['product_url'] = self.url
		a = Zomato_Wrapper(data)
		with open('RealPaprika.json','w') as v:
			json.dump(a.data,v)
		











