from selenium import webdriver
# import selenium.webdriver.common.by 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver.find_element(By.XPATH, '//button[text()="Some text"]')
# driver.find_elements(By.XPATH, '//button')


# driver = webdriver.Firefox()
chromedriver = "/home/vamsi/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.zomato.com/hyderabad/the-indique-bistro-banjara-hills/reviews")
wait = WebDriverWait(driver, 30)
# driver.find_element_by_xpath('//a[@class="item default-section-title everyone empty"]').click()
# f = driver.find_element_by_xpath('//a[@class="item default-section-title everyone empty"]/span[@class="grey-text"]')[0].text
# driver.find_element_by_xpath('//div[@class="load-more bold ttupper tac cursor-pointer fontsize2"]/span[@class="zs-load-more-count"]').click()
p0 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='item default-section-title everyone empty']/span[@class='grey-text']")))
time.sleep(3)
p0.click()
f = driver.find_element_by_xpath('//a[@class="item default-section-title everyone empty"]/span[@class="grey-text"]')
number  = int(f.get_attribute('textContent'))
if number%5 :
	i = number/5
else :
	i = number/5 - 1

while i:
	
	i = i - 1
	
	pr = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='load-more bold ttupper tac cursor-pointer fontsize2']/span[@class='zs-load-more-count']")))
	# time.sleep(3)
	
	pr.click()
# driver.close()
f = driver.find_elements_by_xpath("//div[@class='rev-text-sm mbot0']/div[@class='rev-text-expand ']/a[@class='read-more']")
print f
# for i in (0,range(len(f))):
# 	pr = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='rev-text-sm mbot0']/div[@class='rev-text-expand ']/a[@class='read-more']")))
# 	pr.click()

	
# rm = wait.until(EC.elements_to_be_clickable((By.XPATH, "//div[@class='rev-text-sm mbot0']/div[@class='rev-text-expand ']/a[@class='read-more']")))
