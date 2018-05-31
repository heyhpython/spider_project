# coding: utf-8 
import requests

# url = "http://www.pipl.com/"
url = "http://www.222hhh.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
proxies = {'http': '183.179.199.225'}
resp = requests.get(url, headers=headers, proxies = {'http': '183.179.199.225'}
)
print(resp.text)