import requests
import json
import urllib

locationUrlFromLatLong = 'https://www.zomato.com/php/social_load_more.php'
header = {"origin": "https://www.zomato.com","accept-encoding": "gzip, deflate, br","x-requested-with": "XMLHttpRequest","accept-language": "en-US,en;q=0.8","user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept": "*/*","referer": "https://www.zomato.com/","authority": "www.zomato.com","cookie": "PHPSESSID=5a9b650ae22a5e93455e17813789bef6ba5cf1f9; zl=en; fbtrack=8f0ce9c6e08f18de2db3f5411265aa30; dpr=2; fbcity=6; zone=7000; _ga=GA1.2.1335390262.1470056890; __jpuri=https"%"3A//www.zomato.com/hyderabad/abs-absolute-barbecues-gachibowli; ak_bmsc=61796E271E5B2808717B2DA548BE90E67BB0201F2B7100005E9CCE57317D3021~plLMNw5riwmYTzqLmRJT9Fe7nERBr0lqFT8zmVOOsLMnShQnnivyOWfn8xTspzCIYp5nqJ1ghly5Eg0KjTzB8msnmU6aYuIdYwT5ZRTr4bHMn3ZFM1O2lYUIq0LYQzcjRrS1se1a70/b3oK4/Htj16sWj18lpei4VKwYR9WHHugRY6Wgi+/SIr/6nT8C8ffq3s; bhInfV_cl_id=H0nVMkuW7dqObceMivCXESepxSVESd6hCt0OAMwUsQ5ke3KtEB"}
# --data "entity_id=96858&profile_action=reviews-top&page=0&limit=50"}
response = requests.get(locationUrlFromLatLong, headers=header)
data = response.json()
with open('try.json','w') as v:
	dump(data,v)
