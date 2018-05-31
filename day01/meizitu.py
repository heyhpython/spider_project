import requests
import os
import re

# 封面图http://mm.chinasareview.com/wp-content/uploads/2017a/07/04/limg.jpg
# http://www.meizitu.com/a//5590.html 大图链接
# 页码< li > < a href = '/a/more_1.html' > 2 < / a > < / li > 最大71
# 小图 过滤掉 <img src="http://mm.chinasareview.com/wp-content/uploads/2017a/05/15/limg.jpg"
# 大图保存 http://mm.chinasareview.com/wp-content/uploads/2017a/02/07/09.jpg
'''
妹子图网站的特殊的地方在于网站服务器与图片服务器分开，
任何非网站服务器的对图片资源的请求都会被403  forbiden掉
因此需要在requests中设置代理服务器为网站服务器的ip，避开图片服务器的过滤
'''

# 请求头设置模拟的浏览器版本
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# 创建链接对象
session = requests.session()
# 设置为短链接，防止连接数过多 程序报错
session.keep_alive = False


# 定义函数
def spider_for_meizitu(url):
    '''参数url为页码的链接'''
    print(url)
    response = session.get(url, headers=headers)
    # 获取当前页内容
    page_text = response.text

    # 获取妹子图的链接入口列表
    meiz_urls = re.findall(r'http://www.meizitu.com/a//\d+?.html', page_text)

    for meiz_url in meiz_urls:
        print(meiz_url)
        # 获取图片详情页的页面信息
        detail_response = session.get(meiz_url, headers=headers)
        # 每个图片详情页的大图放在用一个文件夹
        os.makedirs('./meizitu/' + meiz_url[-9:-5], exist_ok=True)
        # 提取出妹子大图链接
        img_urls = re.findall(r'http://mm.chinasareview.com/wp-content/uploads/.*?\d+.jpg', detail_response.text)
        i = 0
        for img_url in img_urls:
            print(img_url)
            # 获取需要的大图，并保存
            img = session.get(img_url, proxies={'http': '27.50.49.210'}, headers=headers)

            path = './meizitu/' + meiz_url[-9:-5] + '/' + str(i) + img_url[-6:]
            with open(path, 'wb') as f:
                f.write(img.content)
                i += 1


for i in range(1, 72):
    page_url = 'http://www.meizitu.com/a/more_%d.html' % i
    spider_for_meizitu(page_url)
