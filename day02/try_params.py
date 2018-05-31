# coding: utf-8 
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

p = {'wd': 'python'}
url = 'http://www.baidu.com'
resp = requests.get(url)
content = resp.content.decode()
print(content)