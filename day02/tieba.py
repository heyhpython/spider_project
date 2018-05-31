# coding: utf-8 
import requests

# https://tieba.baidu.com/f?kw=李毅&ie=utf-8
#
# name = input('贴吧名')
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
#
# for i in range(10):
#     pn = i * 50
#     kw = {'kw': name, 'ie': 'utf-8', 'pn': pn}
#     r = requests.get('https://tieba.baidu.com/f',
#                      params=kw,
#                      headers={
#                          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
#                      )
#
#     with open(str(pn) + '.html', 'w') as f:
#         f.write(r.content.decode())


class TiebaSpidef:
    '''贴吧爬虫类'''

    def __init__(self, name):
        self.name = name

    def get_url_list(self):
        url_list = ['https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(self.name, i * 10) for i in range(10)]
        return url_list

    def parse_url(self, url):
        resp = requests.get(url)
        return resp.content.decode()

    def save_html_str(self, html, page_num):
        path = self.name + '--' + str(page_num) + '.html'
        with open(path, 'w') as f:
            f.write(html)

    def run(self):
        '''执行主要逻辑'''
        # 生成url列表
        url_list = self.get_url_list()

        # 请求url
        for url in url_list:
            html_str = self.parse_url(url)
            self.save_html_str(html_str, url_list.index(url))
            # 保存文件


if __name__ == '__main__':
    tieba_spider = TiebaSpidef('lol')
    tieba_spider.run()
