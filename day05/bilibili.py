# coding: utf-8 
import requests
from lxml import etree
import re

start_url = 'https://m.bilibili.com/bangumi/play/ep7823'
headers = {
    'Referer': 'https://www.bilibili.com/bangumi/play/ep7820',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'finger=846f9182; LIVE_BUVID=AUTO7515275889865517; fts=1527589020; BANGUMI_SS_413_REC=7823; sid=bywgf18g; buvid3=89102350-5F5E-4056-A926-16EEC8780EE8140233infoc; rpdid=oqllxwklspdosimsqlwiw; bg_view_413=7820%7C7819%7C7823%7C7822',
    'Host': 'm.bilibili.com',
}

# resp = requests.get(start_url, headers=headers)
# resp.encoding = 'utf-8'
barrage_url = 'https://comment.bilibili.com/{}.xml'
# xml_str = resp.text
# xml_str = xml_str.replace('encoding="UTF-8"?', '')
# xml = etree.HTML(xml_str)
# barrage_list = xml.xpath('//d/text()')


# cid是如何得到
with open('bili2.html', 'r', encoding='utf-8') as f:
    html_str = f.read()

# html_str = resp.text
html = etree.HTML(html_str)
script = html.xpath('//script[contains(text(),"epList")]/text()')[0]
print(script)
cid_list = re.findall(r'"cid": (\d+)', script)
url_list = [barrage_url.format(i) for i in cid_list[1:]]
for url in url_list:
    barrage_resp = requests.get(url_list)
    barrage_resp.encoding = 'utf-8'
    barrage_str = barrage_resp.text
    barrage_str.replace('encoding="UTF-8"?', '')
    barrage_xml = etree.HTML(barrage_str)
    barrage_list = barrage_xml.xpath('//d/text()')
    with open('barrage.txt', 'a', encoding='utf-8') as f:
        for barrage in barrage_list:
            f.write(barrage)
