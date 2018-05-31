# coding: utf-8 
from selenium import webdriver
import requests
import os
from lxml import etree
import time

class WangYiYunSpider:
    '''爬取所有歌单的信息'''

    def __init__(self):
        self.start_url = 'http://music.163.com/#/discover/playlist'
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=self.option)
        self.url_list = []
        self.a_list = []
        self.dl_list = []
        self.playlist_info_list = []
        self.next_url = ''

    def parse_url(self, url=None):
        if url is None:
            self.driver.get(self.start_url)
        else:
            self.driver.get(url)

        self.driver.switch_to.frame('g_iframe')

    def get_class_a(self, ):
        '''循环大类的列表 获取小类列表'''
        for dl in self.dl_list:
            # 大类名 作为文件夹名 貌似难以取到
            dl_name = dl.find_element_by_xpath('./dt').text
            print('=====')
            print(dl_name)
            # os.makedirs('./{}'.format(dl_name), exist_ok=True)

            # 小类的标签每个a标签代表一个小类信息
            self.a_list.extend(dl.find_elements_by_xpath('./dd/a'))

    def get_class_info(self):
        # 获取小类所在a标签信息
        '''循环每一个a标签'''
        self.url_list = [(a.get_attribute('data-cat'), a.get_attribute('href')) for a in self.a_list]

    def get_palylist_info(self):
        '''获取播放列表'''
        # 每个歌单在一个li标签里
        li_list = self.driver.find_elements_by_xpath('//ul[@id="m-pl-container"]/li')
        for li in li_list:
            playlist_title = li.find_element_by_xpath('.//a[@class="tit f-thide s-fc0"]').text  # 歌单标题
            playlist_author = li.find_element_by_xpath('.//a[@class="nm nm-icn f-thide s-fc3"]').text  # 歌单作者
            playlist_url = li.find_element_by_xpath('.//a[@class="tit f-thide s-fc0"]').get_attribute('href')  # 歌单地址
            author_url = li.find_element_by_xpath('.//a[@class="nm nm-icn f-thide s-fc3"]').get_attribute('href')  # 作者地址
            listener = li.find_element_by_xpath('.//div[@class="bottom"]/span[@class="nb"]').text  # 听了的数量
            self.playlist_info_list.append([playlist_title, listener, playlist_url, playlist_author, author_url])
        self.next_url = self.driver.find_element_by_xpath(
            '//div[@id="m-pl-pager"]//a[@class="zbtn znxt"]').get_attribute('href')

    def save_info(self, class_name):
        '''保存歌单信息 一个小类请求完之后'''
        with open('./playlist/{}'.format(class_name), 'a', encoding='utf-8') as f:
            for playlist in self.playlist_info_list:
                f.write('|'.join(playlist))
                f.write('\n')

    def run(self):
        '''程序运行主逻辑'''

        # 请求初始url,并切换到iframe标签
        self.parse_url()

        # 获取所有大类的名称及下面小类的链接 每一个dl是一个大类
        self.dl_list = self.driver.find_elements_by_xpath('//dl[@class="f-cb"]')

        # 获取小类所在a标签 a_list
        self.get_class_a()

        # 获取小类名及链接信息 self.url_list
        self.get_class_info()

        # 循环self.url_list 的url获取每个小类的页面  每个元素是字典
        print(self.url_list)

        for cate in self.url_list:
            class_name, class_url = cate

            # 请求小类网址
            self.parse_url(url=class_url)
            # todo 要睡一会而才行
            time.sleep(5)

            # 获取歌单信息及下一页地址 self.playlist_info_list
            self.get_palylist_info()

            # 循环获取小类的下一页直至无下一页
            while True:
                print(self.next_url)
                if self.next_url == 'javascript:void(0)':
                    break
                else:
                    self.parse_url(url=self.next_url)
                    #　todo 要睡一会而才行
                    time.sleep(5)
                    self.get_palylist_info()
                    # 将提取到的信息保存到小类对应的文件夹
            self.save_info(class_name)


if __name__ == '__main__':
    spider = WangYiYunSpider()
    spider.run()

# s = [['s', 'd'], ['c', 'x']]
