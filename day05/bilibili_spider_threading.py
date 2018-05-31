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

        # self.proxies = {'https': 'https://115.223.209.238:9000'}
        # 要请求的url队列
        self.url_queue = Queue()
        # 解析出的html字符串队列
        self.html_str_q = Queue()
        # 获取到的弹幕队列
        self.barrage_list_q = Queue()

    def parse_url(self, url=None, headers={}):
        if url is None:
            while True:
                url = self.url_queue.get()
                print(url)
                resp = requests.get(url, headers=headers)
                resp.encoding = 'utf-8'
                self.html_str_q.put(resp.text)
                self.url_queue.task_done()
                return
        else:
            print(url)
            resp = requests.get(url, headers=headers)
            resp.encoding = 'utf-8'
            return resp.text

    def get_cid(self, html_str):
        html = etree.HTML(html_str)
        script = html.xpath('//script[contains(text(),"epList")]/text()')[0]
        # print(script)
        cid_list = re.findall(r'"cid":(\d+)', script)
        return cid_list

    def get_barrage_url(self, cid_list):
        # url_list = [self.barrage_url.format(i) for i in cid_list[1:]]
        for i in cid_list[1:]:
            self.url_queue.put(self.barrage_url.format(i))
            # return url_list

    def get_barrage_list(self):
        while True:
            barrage_str = self.html_str_q.get()
            barrage_str = barrage_str.replace('encoding="UTF-8"?', '')
            # print(barrage_str)
            barrage_xml = etree.HTML(barrage_str)
            barrage_list = barrage_xml.xpath('//d/text()')
            self.barrage_list_q.put(barrage_list)
            self.html_str_q.task_done()
            # return barrage_list

    def save_barrage(self):
        while True:
            barrage_list = self.barrage_list_q.get()
            print(barrage_list)
            with open('barrage2.txt', 'a', encoding='utf-8') as f:
                for barrage in barrage_list:
                    f.write(barrage)
                    f.write('\n')
            print(len(barrage_list))
            print('保存成功')

    def run(self):
        '''主要逻辑'''
        # 请求初始视频url
        html_str = self.parse_url(url=self.start_url, headers=self.headers)
        # print(html_str)

        # 提取数据cid
        cid_list = self.get_cid(html_str)
        print(cid_list)

        # 组织弹幕的url
        self.get_barrage_url(cid_list)
        # 请求网址
        print('==========')
        for i in range(15):
            # barrage_str = self.parse_url(url)
            t_parse = threading.Thread(target=self.parse_url)
            t_parse.setDaemon(True)
            t_parse.start()

            # 提取出信息
        for i in range(2):
            # barrage_list = self.get_barrage_list(barrage_str)
            t_barrage_list = threading.Thread(target=self.get_barrage_list)
            t_barrage_list.setDaemon(True)
            t_barrage_list.start()
        # 写入文件
        for i in range(2):
            # self.save_barrage(barrage_list)
            t_save = threading.Thread(target=self.save_barrage)
            t_save.setDaemon(True)
            t_save.start()
        for q in [self.html_str_q, self.barrage_list_q, self.url_queue]:
            q.join()

        print('主线程结束')

if __name__ == '__main__':
    bili = BiliSpider()
    bili.run()
