# coding: utf-8
import requests
import os
from lxml import etree
import json
from proxies import proxies
import random


class WangYiYunSpider:
    '''爬取所有歌单的信息'''

    def __init__(self):
        self.root_url = 'http://music.163.com'
        self.start_url = 'http://music.163.com/discover/playlist'
        self.classname_list = []  # 所有小类名
        self.class_url = 'http://music.163.com/discover/playlist/?cat={}'
        self.class_url_list = []  # 所有小类url
        self.playlist_urls = []  # 每一小类所有歌单的url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.playlist_info = []
        self.classname = ''
        self.proxies = proxies

    def parse_url(self, url=None):
        if url is None:
            resp = requests.get(self.start_url,
                                headers=self.headers,
                                proxies=random.choice(self.proxies)
                                )
        else:
            resp = requests.get(url, headers=self.headers)
        resp.encoding = 'utf-8'
        return resp.text

    def get_cate_name_list(self, html):
        dl_list = html.xpath('//div[@id="cateListBox"]//dl')
        # print(dl_list)
        for dl in dl_list:
            # cate_name = dl.xpath('./dt/text()')[0]
            classname_list = dl.xpath('./dd/a/text()')
            self.classname_list.extend(classname_list)
        print(self.classname_list)

    def get_class_url(self):
        for classname in self.classname_list:
            self.class_url_list.append(self.class_url.format(classname))

    def get_playlist(self, html):
        '''获取歌单链接及下一页url'''

        # 歌单标题
        # /playlist?id=2174792139" 要加上root_url
        playlist_url = html.xpath('//ul[@id="m-pl-container"]//a[@class="msk"]/@href')
        self.playlist_urls.extend(playlist_url)
        # print(playlist_url)

        try:
            next_url = html.xpath('//a[@class="zbtn znxt"]/@href')[0]
        except:
            return None
        else:
            return self.root_url + next_url

    def get_playlist_info(self):
        # 循环请求歌单详情
        info_dict = {}
        for url in self.playlist_urls:
            # 请求url 获取网页
            url = self.root_url + url
            html_str = self.parse_url(url=url)
            html = etree.HTML(html_str)

            # 从网页中提取信息
            songs = []
            songs_li = html.xpath('//div[@id="song-list-pre-cache"]//li')
            for li in songs_li:
                song_info = {
                                'song_name': li.xpath('.//text()'),
                                'song_link': li.xpath('./a/@href')

                            },
                songs.append(song_info)

            info_dict = {
                'class': self.classname,
                'title': html.xpath('//title/text()'),
                'url': url,
                'author': html.xpath('//div[@class="user f-cb"]/a[@class="s-fc7"]/text()'),
                'create_time': html.xpath('//div[@class="user f-cb"]/span[@class="u-icn u-icn-84 "]/text()'),
                'tags': html.xpath('//div[@clas="tags f-cb"]/b//text()'),
                'description': html.xpath('//p[@id="album-desc-dot"]/text()'),
                'transmit': html.xpath('//a[@class="u-btni u-btni-share "]/i/text()'),
                'store': html.xpath('//a[@class="u-btni u-btni-fav "]/i/text()'),
                'comments': html.xpath('//span[@id="cnt_comment_count"]/text()'),
                'played_times': html.xpath('//strong[@id="play-count"]/text()'),
                'songs': songs
            }
            self.playlist_info.append(info_dict)
        # 清空url列表
        self.playlist_urls = []

    def save_palylist_info(self):
        '''保存歌单信息'''
        with open('{}.json'.format(self.classname), 'a', encoding='utf-8') as f:
            f.write(json.dumps(self.playlist_info, ensure_ascii=False, indent=4))

    def run(self):
        '''程序运行主逻辑'''
        # 请求初始url
        html_str = self.parse_url()
        html = etree.HTML(html_str)
        # print(html)

        # 获取所有分类名
        self.get_cate_name_list(html)

        # 组织没各小类的url get_class_url
        # print(self.classname_list)
        self.get_class_url()

        # 遍历url列表获取每小类的首页页面
        '''
        每个大类一个文件夹
        每个小类一个json文件
        每个歌单一条数据
        没首歌在歌单里一个字段
        '''
        # print(self.class_url_list)
        for url in self.class_url_list:
            print(url)
            # 请求小类url
            html_str = self.parse_url(url=url)
            html = etree.HTML(html_str)
            # 小类名 作为文件名
            self.classname = html.xpath('//span[@class="f-ff2 d-flag"]/text()')[0]

            # 　获取歌单链接及下一页url
            next_url = self.get_playlist(html)

            # 重复的请求与获取 直到没有下一页
            while True:
                if next_url:
                    html_str = self.parse_url(url=next_url)
                    html = etree.HTML(html_str)

                    # 　获取歌单链接及下一页url
                    next_url = self.get_playlist(html)
                    print(next_url)
                else:
                    break

            # 请求歌单列表里的歌单url 进入详情页面
            self.get_playlist_info()
            # 获取详情页的信息并保存
            self.save_palylist_info()


if __name__ == '__main__':
    spider = WangYiYunSpider()
    spider.run()

# s = [['s', 'd'], ['c', 'x']]
