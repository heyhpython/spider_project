# coding: utf-8
import requests
import json
# query:hello
url = 'http://fanyi.baidu.com/langdetect'
params = {'query': 'hello'}
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
resp = requests.post(url, params=params)
lang = json.loads(resp.content.decode())['lan']
print(lang)