from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from zomato_format import Zomato_Reviews_Format


class Zomato_Complete_Scrapper():
	def __init__(self,restaurant_url):
		self.restaurant_url = restaurant_url
		self.Scrapper()
	def Scrapper(self):
		chromedriver = "/home/vamsi/Downloads/chromedriver"
		driver = webdriver.Chrome(chromedriver)
		driver.get(self.restaurant_url)
		wait = WebDriverWait(driver, 30)

		dct = {}
		dct['product_url'] = self.restaurant_url
		data = []

		try :
			#Locating the path for reviews
			# If it is unable to find reviews tab then it will go to except block and print no reviews
			p0 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='item default-section-title everyone empty']/span[@class='grey-text']")))
			time.sleep(3)
			p0.click()

			#For finding out number of reviews
			f = driver.find_element_by_xpath('//a[@class="item default-section-title everyone empty"]/span[@class="grey-text"]')
			number  = int(f.get_attribute('textContent'))
			if number%5 :
				i = number/5
			else :
				i = number/5 - 1

			# load more section for extracting all the reviews
			while i:
				i = i - 1
				pr = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='load-more bold ttupper tac cursor-pointer fontsize2']/span[@class='zs-load-more-count']")))
				pr.click()

			#for all the reviews
			f = driver.find_elements_by_xpath('//div[@class="rev-text mbot0 "]')
			for v in range(0,len(f)):
				g = (f[v].get_attribute('textContent').strip())
				h = g.split('\n')
				b = h[1:]
				k = ''.join(b)
				c = k.strip().split('.')
				for i in range(0,len(c)):
					c[i] = c[i].strip()
				data.append({'text':'.'.join(c)})

			# for rating of the user
			avoiding_none = 0
			itr = 0
			rating = driver.find_elements_by_xpath('//div[@class="rev-text mbot0 "]/div')
			count = min(len(data),len(rating))
			for rate in range(0,count):
				rating_sample = rating[rate].get_attribute('aria-label')
				title = rating[rate].get_attribute('title')
				if not avoiding_none:
					data[itr].update({'title': title})
					data[itr].update({'rating': rating_sample.split(' ')[1]})
					itr += 1
					avoiding_none = 1
				else:
					avoiding_none = 0

			# for review_url 
			avoiding_none = 0
			itr = 0
			review_url = driver.find_elements_by_xpath('//a[@class="grey-text"]')
			count = min(len(data),len(review_url))
			for i in range(0,count):
				url = review_url[i].get_attribute('href')
				if not avoiding_none:
					data[itr].update({'url': url})
					itr += 1
					avoiding_none = 1
				else:
					avoiding_none = 0

			#For review date
			review_date = driver.find_elements_by_xpath('//a[@class="grey-text"]/time')
			count = min(len(data),len(review_date))
			for i in range(0,count):
				data[i].update({'date':review_date[i].get_attribute('datetime')})

			# For Promotes
			promotes = driver.find_elements_by_xpath('//div[@data-action_type="REVIEW"]')
			count = min(len(data),len(promotes))
			for i in range(0,count):
				data[i].update({'promotes':promotes[i].get_attribute('aria-label').split(' ')[0]})

			# For Comments
			comments = driver.find_elements_by_xpath('//div[@class="ui basic label stats-comment"]')
			count = min(len(data),len(comments))
			for i in range(0,count):
				data[i].update({'comments':comments[i].get_attribute('aria-label').split(' ')[0]})
			itemprop="name"

			# For Name of the user
			name_user = driver.find_elements_by_xpath('//a[@itemprop="name"]')
			count = min(len(data),len(name_user))
			for i in range(0,count):
				data[i].update({'user':{'name':name_user[i].get_attribute('textContent').strip()}})

			# For number of reviews and number of followers 
			review_number = driver.find_elements_by_xpath('//span[@class="grey-text fontsize5 nowrap"]')
			count = min(len(data),len(review_number))
			for i in range(0,count):
				d = review_number[i].get_attribute('textContent').strip().split('\n')
				if len(d) > 1:
					data[i]['user'].update({'reviews_count':d[0].split(' ')[0]})
					data[i]['user'].update({'followers_count':d[2].strip().split(' ')[0]})
				elif len(d) == 1:
					data[i]['user'].update({'reviews_count':d[0].split(' ')[0]})
					data[i]['user'].update({'followers_count':0})

			# For url of the user
			url_user = driver.find_elements_by_xpath('//div[@class="header nowrap ui left"]/a')
			count = min(len(data),len(url_user))
			for i in range(0,count):
				data[i]['user'].update({'url':url_user[i].get_attribute('href')})

			#Json file creation
			dct['reviews'] = data
			with open('test.json','w') as j:
				json.dump(dct,j)
			driver.close()
			Zomato_Reviews_Format('test.json')
		except:
			print 'No reviews'
			




















# driver.find_element_by_class_name('zs-load-more-count').click()
# driver.find_element_by_xpath('//a[@class="item default-section-title everyone empty"]').click()
# f = driver.find_element_by_xpath('//a[@class="item default-section-title everyone empty"]/span[@class="grey-text"]')[0].text
# driver.find_element_by_xpath('//div[@class="load-more bold ttupper tac cursor-pointer fontsize2"]/span[@class="zs-load-more-count"]').click()
# r = urllib.urlopen('https://www.zomato.com/hyderabad/the-indique-bistro-banjara-hills/reviews').read()
# text = soup.find_all("div", class_="rev-text mbot0 ")
# for element in text:
# 	tmp1 = element.get_text().strip()
# 	tmp2 = tmp1.split('\n')
# 	tmp3 = tmp2[1:]
# 	tmp4 = ''.join(tmp3)
# 	tmp5 = tmp4.strip.split('.')
# 	for i in range(0,len(tmp5)):
# 		tmp5[i] = tmp5[i].strip()
# 	data.append({'text':'.'.join(tmp5)})