# coding: utf-8 
import requests

# https://tieba.baidu.com/f?kw=李毅&ie=utf-8

name = input('贴吧名')

r = requests.get('https://tieba.baidu.com/f?kw=%s&ie=utf-8' % name)
r.encoding = 'utf8'
print(r.text)