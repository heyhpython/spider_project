# coding: utf-8 
import requests
from lxml import etree


class BaiduSpider:
    '''百度贴吧爬虫'''

    def __init__(self):
        self.base_url = 'http://tieba.baidu.com'
        # self.headers = {
        #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def parse_url(self, url):
        '''请求url 返回element对象'''
        response = requests.get(url).content.decode()
        # print(response)
        html_ele = etree.HTML(response)
        # print(etree.tostring(html_ele).decode())
        return html_ele

    def write_url(self, url_list):
        '''写入url列表'''
        with open('baidu.txt', 'a', encoding='utf-8') as f:
            for img_url in url_list:
                f.write(img_url)
                f.write('\n')
            print('保存成功')

    def run(self):
        url = 'http://tieba.baidu.com/f?kw=猫'
        while url:
            # 获取列表页面的所有元素
            list_html_ele = self.parse_url(url)

            # 1.获取当前页的所有帖子链接 要拼接
            article_url_list = list_html_ele.xpath(
                '//ul[@id="thread_list"]//a[@class="j_th_tit "]/@href')

            # 2.请求链接，解析出元素，提取出图片的链接并保存
            for article_url in article_url_list:
                # 拼接url地址
                detail_url = self.base_url + article_url

                # 获取帖子详情页的元素
                detail_html_ele = self.parse_url(detail_url)

                # 提取出所有的用户图片的地址 不用拼接
                user_img_url_list = detail_html_ele.xpath(
                    '//div[contains(@id,"post_content_")]/img[@class="BDE_Image"]/@src')

                # 写入文件
                self.write_url(user_img_url_list)

            # 获取下一页链接 重复1,2步，直至没有下一页 要拼接
            try:
                url = list_html_ele.xpath('//*[@id="frs_list_pager"]/a[@class="next pagination-item "]/@href')[0]
            except:
                print('no more page')
                break


if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()
