# coding: utf-8 
import requests
from lxml import etree


def parse_url(url):
    '''请求url 返回element对象'''
    response = requests.get(url).content.decode()
    html_ele = etree.HTML(response)
    print(etree.tostring(html_ele))
    return html_ele


# # 获取列表页面的所有元素
# list_html_ele = parse_url(url)
#
# # 1.获取当前页的所有帖子链接 要拼接
# article_url_list = list_html_ele.xpath('//ul[@id="thread_list"]//a[@class="j_th_tit "]/@href')


# 2.请求链接，解析出元素，提取出图片的链接并保存
# for article_url in article_url_list:
#     # 拼接url地址
#     url = base_url + article_url
#     # 获取帖子详情页的元素
#     detail_html_ele = parse_url(url)
#     # 提取出所有的用户图片的地址 不用拼接
#     user_img_url_list = detail_html_ele.HTML('//div[contains(@id,"post_content_")]/img[@class="BDE_Image"]/@src')
#
# # 获取下一页链接 重复1,2步，直至没有下一页 要拼接
# next_url = list_html_ele.HTML('//*[@id="frs_list_pager"]/a[@class="next pagination-item "]/@href')

base_url = 'http://tieba.baidu.com'
# 1. 请求猫吧首页url
url = 'http://tieba.baidu.com/f?kw=猫'
while True:
    # 获取列表页面的所有元素
    print(url)
    list_html_ele = parse_url(url)

    # 1.获取当前页的所有帖子链接 要拼接
    article_url_list = list_html_ele.xpath('//ul[@id="thread_list"]//a[@class="j_th_tit "]/@href')
    print(article_url_list)

    # 2.请求链接，解析出元素，提取出图片的链接并保存
    for article_url in article_url_list:
        # 拼接url地址
        detail_url = base_url + article_url
        print(detail_url)

        # 获取帖子详情页的元素
        detail_html_ele = parse_url(detail_url)
        print(detail_html_ele)

        # 提取出所有的用户图片的地址 不用拼接
        user_img_url_list = detail_html_ele.xpath('//div[contains(@id,"post_content_")]/img[@class="BDE_Image"]/@src')
        # parse_url(user_img_url_list)

        # 写入文件
        with open('baidu.txt', 'a', encoding='utf-8') as f:
            for img_url in user_img_url_list:
                f.write(img_url)
            print('保存成功')

    # 获取下一页链接 重复1,2步，直至没有下一页 要拼接
    try:
        url = list_html_ele.xpath('//*[@id="frs_list_pager"]/a[@class="next pagination-item "]/@href')[0]
        url = 'http:' + url
    except:
        print('no more page')
        break
