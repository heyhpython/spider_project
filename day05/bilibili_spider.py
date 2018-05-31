# coding: utf-8 
import re
import requests
from lxml import etree
import threading
from queue import Queue


class BiliSpider:
    '''哔哩哔哩弹幕爬虫'''

    def __init__(self):
        self.start_url = 'https://m.bilibili.com/bangumi/play/ep7823'

        self.headers = {
            'Referer': 'https://www.bilibili.com/bangumi/play/ep7820',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'finger=846f9182; LIVE_BUVID=AUTO7515275889865517; fts=1527589020; BANGUMI_SS_413_REC=7823; sid=bywgf18g; buvid3=89102350-5F5E-4056-A926-16EEC8780EE8140233infoc; rpdid=oqllxwklspdosimsqlwiw; bg_view_413=7820%7C7819%7C7823%7C7822',
            'Host': 'm.bilibili.com',
        }

        self.barrage_url = 'https://comment.bilibili.com/{}.xml'

        self.proxies = {'https': 'https://115.223.209.238:9000'}

    def parse_url(self, url, headers={}):

        print(url)
        # resp = requests.get(url, headers=headers, proxies=self.proxies)
        resp = requests.get(url, headers=headers)
        resp.encoding = 'utf-8'
        return resp.text

    def get_cid(self, html_str):
        html = etree.HTML(html_str)
        script = html.xpath('//script[contains(text(),"epList")]/text()')[0]
        print(script)
        cid_list = re.findall(r'"cid":(\d+)', script)
        return cid_list

    def get_barrage_url(self, cid_list):
        url_list = [self.barrage_url.format(i) for i in cid_list[1:]]
        return url_list

    def get_barrage_list(self, barrage_str):
        barrage_str = barrage_str.replace('encoding="UTF-8"?', '')
        print(barrage_str)
        barrage_xml = etree.HTML(barrage_str)
        barrage_list = barrage_xml.xpath('//d/text()')
        return barrage_list

    def save_barrage(self, barrage_list):
        # with open('barrage.txt', 'a', encoding='utf-8') as f:
        # for barrage in barrage_list:
        #     f.write(barrage)
        #     f.write('\n')
        print('保存成功')

    def run(self):
        '''主要逻辑'''
        # 请求初始视频url
        html_str = self.parse_url(self.start_url, self.headers)
        # print(html_str)
        # 提取数据cid
        cid_list = self.get_cid(html_str)

        # 组织弹幕的url
        barrage_url_list = self.get_barrage_url(cid_list)
        # 请求网址
        for url in barrage_url_list:
            barrage_str = self.parse_url(url)

            # 提取出信息
            barrage_list = self.get_barrage_list(barrage_str)

            # 写入文件
            self.save_barrage(barrage_list)


bili = BiliSpider()
bili.run()
