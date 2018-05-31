# coding: utf-8 
# from parse import parse_url
import json
import requests

# url = 'https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=18&count=18'
# html_str = parse_url(url)
# file_data = json.loads(html_str)
# with open('douban.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(file_data["subject_collection_items"], indent=4, ensure_ascii=False))
#
# refer = "https://m.douban.com/tv/"

# Request_URL = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?start=0&count=18'
# Request_URL2 = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?start=18&count=18'
# Request_URL_en1 = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_english_hot/items?start=0&count=18'
# Request_URL_ko = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_korean_drama_hot/items?start=0&count=18'
# Request_URLcn = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?start=0&count=18'


# 定义写文件函数
# def write_data(file_dict, filename):
#     '''定义文件写入函数 传入一个字典'''
#     with open(filename, 'w', encoding='utf-8') as f:
#         f.write(json.dumps(file_dict["subject_collection_items"], indent=4, ensure_ascii=False))
#
#
# tv_list = ['american', 'english', 'korean_drama', 'domestic']
# for country in tv_list:
#     # 组织url
#     url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_{}_hot/items?start=0&count=18'.format(
#         country)
#
#     # 先请求页面获取总数
#     html_str = parse_url(url)
#     # 解析数据
#     file_dict = json.loads(html_str)
#     total = file_dict['total']
#     print(total)
#     step = 18
#     for i in range(18, int(total), step):
#         # 写入上次获取到的数据
#         write_data(file_dict, country + '{}.json'.format(i / 18))
#         # 重新组织url
#         if i + 18 >= int(total):
#             count = int(total) - i
#             url = url.replace('start={}&count=18'.format(i - 18), 'start={}&count={}'.format(i, count))
#         else:
#             url = url.replace('start={}'.format(i - 18), 'start={}'.format(i))
#         # 请求url
#         html_str = parse_url(url)
#         # 解析数据
#         file_dict = json.loads(html_str)
import json
import requests


class TvSpider:
    '''豆瓣电视爬虫'''

    def __init__(self, country):
        '''
        爬虫类的初始化
        :param country: 要爬去的国家，命名需与豆瓣的相契合
        '''
        # 要爬取的电视的国家全称
        self.country = country
        # 要爬去电视列表的第一页 在豆瓣电视剧的列表也找到items开头的请求，
        self.url = 'https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_{}_hot/items?start={}&count=18'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
            # 关联的url，必须加，否则豆瓣的反扒措施会让你一无所获
            "Referer": "https://m.douban.com/tv/"}

    def write_data(self, file_dict, filename):
        '''定义文件写入函数 传入一个字典 和文件名'''
        # print(json.dumps(file_dict["subject_collection_items"]))
        content_list = file_dict["subject_collection_items"]
        with open(filename, 'a', encoding='utf-8') as f:
            for item in content_list:
                f.write(json.dumps(item, ensure_ascii=False, indent=4))
                f.write('\n')

    def parse_url(self, url):
        '''请求网址 获取返回的json数据'''
        print(url)
        try:
            # 发出get请求 获取数据
            html_str = requests.get(url, verify=False, headers=self.headers, )
            html_str.encoding = 'utf-8'
            return html_str.text
        except Exception as e:
            html_str = None
            print(e)
            return html_str

    def run(self):
        '''爬取的主要逻辑'''
        # 1.根据初始化的country获取地一页数据及电视剧的总数量
        # 组织url
        num = 0
        total = 100
        # url = self.url.format(self.country, num)
        # html_str = self.parse_url(self.url)
        # # 解析数据
        # file_dict = json.loads(html_str)
        # total = file_dict['total']
        # 豆瓣每一页的数量
        # step = 18
        # print(total)
        # for i in range(18, int(total), step):
        #     # 写入上次获取到的数据
        #     self.write_data(file_dict, self.country + '{}.json'.format(int(i / 18)))
        #     # 重新组织url
        #     if i + 18 >= int(total):
        #         count = int(total) - i
        #         url = self.url.replace('start={}&count=18'.format(i - 18), 'start={}&count={}'.format(i, count))
        #     else:
        #         url = self.url.replace('start={}'.format(i - 18), 'start={}'.format(i))
        #     # 请求url
        #     print(url)
        #     html_str = self.parse_url(url)
        #     # 解析数据
        #     file_dict = json.loads(html_str)
        #     #
        while num < total:
            url = self.url.format(self.country, num)
            html_str = self.parse_url(url)
            # 解析数据
            file_dict = json.loads(html_str)

            total = file_dict['total']
            total = int(total)
            self.write_data(file_dict, self.country + '.txt')
            num += 18


if __name__ == '__main__':
    # american 是豆瓣在设计url时设计的美国地区对应的名，需要观察各个地区的名，来获取其他地区
    # 此处仅仅作为示范
    spider = TvSpider('american')
    spider.run()
    # <a target="_blank" href="https://www.guokr.com/question/669761/">
    # "https://www.guokr.com/question/668829/">狗<
