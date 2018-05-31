# coding: utf-8 
import requests
from lxml import etree

resp = requests.get('http://www.xicidaili.com/wt/', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'})

html = etree.HTML(resp.content.decode())
print(resp.content.decode())
tr_list = html.xpath('//table[@id="ip_list"]//tr')
proxies = []
for tr in tr_list[1:]:
    ip = tr.xpath('./td[2]/text()')
    port = tr.xpath('./td[3]/text()')
    protocol = tr.xpath('./td[6]/text()')
    if (len(port) + len(ip) +len(protocol)) > 0:
        proxies.append({
            protocol[0]: ip[0] + ':' + port[0]
        })
print(proxies)

