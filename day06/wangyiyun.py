# coding: utf-8 
from selenium import webdriver
import requests
import os
from lxml import etree

start_url = 'http://music.163.com/#/discover/playlist'
start_url = 'http://music.163.com/#/discover/playlist/?cat=%E6%AC%A7%E7%BE%8E'

driver = webdriver.Chrome()
driver.get(start_url)
driver.switch_to.frame('g_iframe')
# 获取所有大类的标签 大文件夹
dl_list = driver.find_elements_by_xpath('//dl[@class="f-cb"]')
# 循环列表 获取大类里的小类
category_list = []
for category in dl_list:
    # {"category_name":[data_cate_list]}
    # data_cate_list=[{data_cate_name:href}]
    category_name = category.find_element_by_xpath('./dt').text
    a_list = category.find_elements_by_xpath('./dd/a')
    data_cate_list = [{a.text: a.get_attribute('href')} for a in a_list]
    category_list.append({category_name: data_cate_list})
    print(category_list)
    # print({category_name: data_cate_list})
# print(category_list)
# 循环获取列表中的url
# 每一大类一个大文件夹 里面的每个小类一个文件
for category in category_list:
    # 语种、风格、场景、情感、主题 category是一个字典
    for cate_name, class_list in category.items():
        os.makedirs('./{}'.format(cate_name), exist_ok=True)
        for class_dict in class_list:
            '''循环小类列表 获取小类名及url地址'''
            for class_name, url in class_dict:
                # 请求url
                driver.get(url)
                # resp = requests.get(url)
                # html_str = resp.content.encode()
                # 获取html元素
                # html = etree.HTML(html_str)
                driver.switch_to.frame('g_iframe')
                # 获取信息
                # li_list = html.xpath('')
                li_list = driver.find_elements_by_xpath('//ul[@id="m-pl-container"]/li')
                for li in li_list:
                    playlist_title = li.find_element_by_xpath('./a[@class="tit f-thide s-fc0"]').text  # 歌单标题
                    playlist_author = li.find_element_by_xpath('./a[@class="nm nm-icn f-thide s-fc3"]').text  #歌单作者
                    playlist_url = li.find_element_by_xpath('./a[@class="tit f-thide s-fc0"]').get_attribute('href')  # 歌单地址
                    author_url = li.find_element_by_xpath('./a[@class="nm nm-icn f-thide s-fc3"]').get_attribute('href')  # 作者地址
                    listener = li.find_element_by_xpath('.//div[@class="bottom"]/span[@class="nb"]').text # 听了的数量
                    with open('./{}/{}.txt'.format(cate_name, class_name), 'a', encoding='utf-8') as f:
                        f.write('|'.join([playlist_title, listener, playlist_url, playlist_author, author_url]))
