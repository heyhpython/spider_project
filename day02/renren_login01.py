# coding: utf-8 
import requests

url = 'http://www.renren.com/PLogin.do'
data = {
    'email': '18842691265',
    'password': 'WS1204HYH0826'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
session = requests.session()
session.post(url, data=data,headers=headers)
resp = session.get('http://www.renren.com/424218344', headers=headers)
print(resp.content.decode())