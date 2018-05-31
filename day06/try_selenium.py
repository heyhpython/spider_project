# coding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome import options
import time



driver = webdriver.Chrome()

driver.get('http:www.baidu.com')

# 设置窗口大小
# driver.set_window_size(1080*960)

# 最大化窗口
driver.maximize_window()

# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_id('su').click()
driver.save_screenshot('./baidu.png')

cookies = driver.get_cookies()
print(cookies)

cookies = {name: value for i in cookies for name, value in i.get_items()}

cate = [
    {'语种': [{'华语': 'http://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD'},
            {'欧美': 'http://music.163.com/discover/playlist/?cat=%E6%AC%A7%E7%BE%8E'},
            {'日语': 'http://music.163.com/discover/playlist/?cat=%E6%97%A5%E8%AF%AD'},
            {'韩语': 'http://music.163.com/discover/playlist/?cat=%E9%9F%A9%E8%AF%AD'},
            {'粤语': 'http://music.163.com/discover/playlist/?cat=%E7%B2%A4%E8%AF%AD'},
            {'小语种': 'http://music.163.com/discover/playlist/?cat=%E5%B0%8F%E8%AF%AD%E7%A7%8D'}]},
    {'风格': [{'流行': 'http://music.163.com/discover/playlist/?cat=%E6%B5%81%E8%A1%8C'},
            {'摇滚': 'http://music.163.com/discover/playlist/?cat=%E6%91%87%E6%BB%9A'},
            {'民谣': 'http://music.163.com/discover/playlist/?cat=%E6%B0%91%E8%B0%A3'},
            {'电子': 'http://music.163.com/discover/playlist/?cat=%E7%94%B5%E5%AD%90'},
            {'舞曲': 'http://music.163.com/discover/playlist/?cat=%E8%88%9E%E6%9B%B2'},
            {'说唱': 'http://music.163.com/discover/playlist/?cat=%E8%AF%B4%E5%94%B1'},
            {'轻音乐': 'http://music.163.com/discover/playlist/?cat=%E8%BD%BB%E9%9F%B3%E4%B9%90'},
            {'爵士': 'http://music.163.com/discover/playlist/?cat=%E7%88%B5%E5%A3%AB'},
            {'乡村': 'http://music.163.com/discover/playlist/?cat=%E4%B9%A1%E6%9D%91'},
            {'R&B/Soul': 'http://music.163.com/discover/playlist/?cat=R%26B%2FSoul'},
            {'古典': 'http://music.163.com/discover/playlist/?cat=%E5%8F%A4%E5%85%B8'},
            {'民族': 'http://music.163.com/discover/playlist/?cat=%E6%B0%91%E6%97%8F'},
            {'英伦': 'http://music.163.com/discover/playlist/?cat=%E8%8B%B1%E4%BC%A6'},
            {'金属': 'http://music.163.com/discover/playlist/?cat=%E9%87%91%E5%B1%9E'},
            {'朋克': 'http://music.163.com/discover/playlist/?cat=%E6%9C%8B%E5%85%8B'},
            {'蓝调': 'http://music.163.com/discover/playlist/?cat=%E8%93%9D%E8%B0%83'},
            {'雷鬼': 'http://music.163.com/discover/playlist/?cat=%E9%9B%B7%E9%AC%BC'},
            {'世界音乐': 'http://music.163.com/discover/playlist/?cat=%E4%B8%96%E7%95%8C%E9%9F%B3%E4%B9%90'},
            {'拉丁': 'http://music.163.com/discover/playlist/?cat=%E6%8B%89%E4%B8%81'},
            {'另类/独立': 'http://music.163.com/discover/playlist/?cat=%E5%8F%A6%E7%B1%BB%2F%E7%8B%AC%E7%AB%8B'},
            {'New Age': 'http://music.163.com/discover/playlist/?cat=New%20Age'},
            {'古风': 'http://music.163.com/discover/playlist/?cat=%E5%8F%A4%E9%A3%8E'},
            {'后摇': 'http://music.163.com/discover/playlist/?cat=%E5%90%8E%E6%91%87'},
            {'Bossa Nova': 'http://music.163.com/discover/playlist/?cat=Bossa%20Nova'}]},
    {'场景': [{'清晨': 'http://music.163.com/discover/playlist/?cat=%E6%B8%85%E6%99%A8'},
            {'夜晚': 'http://music.163.com/discover/playlist/?cat=%E5%A4%9C%E6%99%9A'},
            {'学习': 'http://music.163.com/discover/playlist/?cat=%E5%AD%A6%E4%B9%A0'},
            {'工作': 'http://music.163.com/discover/playlist/?cat=%E5%B7%A5%E4%BD%9C'},
            {'午休': 'http://music.163.com/discover/playlist/?cat=%E5%8D%88%E4%BC%91'},
            {'下午茶': 'http://music.163.com/discover/playlist/?cat=%E4%B8%8B%E5%8D%88%E8%8C%B6'},
            {'地铁': 'http://music.163.com/discover/playlist/?cat=%E5%9C%B0%E9%93%81'},
            {'驾车': 'http://music.163.com/discover/playlist/?cat=%E9%A9%BE%E8%BD%A6'},
            {'运动': 'http://music.163.com/discover/playlist/?cat=%E8%BF%90%E5%8A%A8'},
            {'旅行': 'http://music.163.com/discover/playlist/?cat=%E6%97%85%E8%A1%8C'},
            {'散步': 'http://music.163.com/discover/playlist/?cat=%E6%95%A3%E6%AD%A5'},
            {'酒吧': 'http://music.163.com/discover/playlist/?cat=%E9%85%92%E5%90%A7'}]},
    {'情感': [{'怀旧': 'http://music.163.com/discover/playlist/?cat=%E6%80%80%E6%97%A7'},
            {'清新': 'http://music.163.com/discover/playlist/?cat=%E6%B8%85%E6%96%B0'},
            {'浪漫': 'http://music.163.com/discover/playlist/?cat=%E6%B5%AA%E6%BC%AB'},
            {'性感': 'http://music.163.com/discover/playlist/?cat=%E6%80%A7%E6%84%9F'},
            {'伤感': 'http://music.163.com/discover/playlist/?cat=%E4%BC%A4%E6%84%9F'},
            {'治愈': 'http://music.163.com/discover/playlist/?cat=%E6%B2%BB%E6%84%88'},
            {'放松': 'http://music.163.com/discover/playlist/?cat=%E6%94%BE%E6%9D%BE'},
            {'孤独': 'http://music.163.com/discover/playlist/?cat=%E5%AD%A4%E7%8B%AC'},
            {'感动': 'http://music.163.com/discover/playlist/?cat=%E6%84%9F%E5%8A%A8'},
            {'兴奋': 'http://music.163.com/discover/playlist/?cat=%E5%85%B4%E5%A5%8B'},
            {'快乐': 'http://music.163.com/discover/playlist/?cat=%E5%BF%AB%E4%B9%90'},
            {'安静': 'http://music.163.com/discover/playlist/?cat=%E5%AE%89%E9%9D%99'},
            {'思念': 'http://music.163.com/discover/playlist/?cat=%E6%80%9D%E5%BF%B5'}]},
    {'主题': [{'影视原声': 'http://music.163.com/discover/playlist/?cat=%E5%BD%B1%E8%A7%86%E5%8E%9F%E5%A3%B0'},
            {'ACG': 'http://music.163.com/discover/playlist/?cat=ACG'},
            {'儿童': 'http://music.163.com/discover/playlist/?cat=%E5%84%BF%E7%AB%A5'},
            {'校园': 'http://music.163.com/discover/playlist/?cat=%E6%A0%A1%E5%9B%AD'},
            {'游戏': 'http://music.163.com/discover/playlist/?cat=%E6%B8%B8%E6%88%8F'},
            {'70后': 'http://music.163.com/discover/playlist/?cat=70%E5%90%8E'},
            {'80后': 'http://music.163.com/discover/playlist/?cat=80%E5%90%8E'},
            {'90后': 'http://music.163.com/discover/playlist/?cat=90%E5%90%8E'},
            {'网络歌曲': 'http://music.163.com/discover/playlist/?cat=%E7%BD%91%E7%BB%9C%E6%AD%8C%E6%9B%B2'},
            {'KTV': 'http://music.163.com/discover/playlist/?cat=KTV'},
            {'经典': 'http://music.163.com/discover/playlist/?cat=%E7%BB%8F%E5%85%B8'},
            {'翻唱': 'http://music.163.com/discover/playlist/?cat=%E7%BF%BB%E5%94%B1'},
            {'吉他': 'http://music.163.com/discover/playlist/?cat=%E5%90%89%E4%BB%96'},
            {'钢琴': 'http://music.163.com/discover/playlist/?cat=%E9%92%A2%E7%90%B4'},
            {'器乐': 'http://music.163.com/discover/playlist/?cat=%E5%99%A8%E4%B9%90'},
            {'榜单': 'http://music.163.com/discover/playlist/?cat=%E6%A6%9C%E5%8D%95'},
            {'00后': 'http://music.163.com/discover/playlist/?cat=00%E5%90%8E'}]}]
url_list = [{'华语': 'http://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD'},
            {'欧美': 'http://music.163.com/discover/playlist/?cat=%E6%AC%A7%E7%BE%8E'},
            {'日语': 'http://music.163.com/discover/playlist/?cat=%E6%97%A5%E8%AF%AD'},
            {'韩语': 'http://music.163.com/discover/playlist/?cat=%E9%9F%A9%E8%AF%AD'},
            {'粤语': 'http://music.163.com/discover/playlist/?cat=%E7%B2%A4%E8%AF%AD'},
            {'小语种': 'http://music.163.com/discover/playlist/?cat=%E5%B0%8F%E8%AF%AD%E7%A7%8D'},
            {'流行': 'http://music.163.com/discover/playlist/?cat=%E6%B5%81%E8%A1%8C'},
            {'摇滚': 'http://music.163.com/discover/playlist/?cat=%E6%91%87%E6%BB%9A'},
            {'民谣': 'http://music.163.com/discover/playlist/?cat=%E6%B0%91%E8%B0%A3'},
            {'电子': 'http://music.163.com/discover/playlist/?cat=%E7%94%B5%E5%AD%90'},
            {'舞曲': 'http://music.163.com/discover/playlist/?cat=%E8%88%9E%E6%9B%B2'},
            {'说唱': 'http://music.163.com/discover/playlist/?cat=%E8%AF%B4%E5%94%B1'},
            {'轻音乐': 'http://music.163.com/discover/playlist/?cat=%E8%BD%BB%E9%9F%B3%E4%B9%90'},
            {'爵士': 'http://music.163.com/discover/playlist/?cat=%E7%88%B5%E5%A3%AB'},
            {'乡村': 'http://music.163.com/discover/playlist/?cat=%E4%B9%A1%E6%9D%91'},
            {'R&B/Soul': 'http://music.163.com/discover/playlist/?cat=R%26B%2FSoul'},
            {'古典': 'http://music.163.com/discover/playlist/?cat=%E5%8F%A4%E5%85%B8'},
            {'民族': 'http://music.163.com/discover/playlist/?cat=%E6%B0%91%E6%97%8F'},
            {'英伦': 'http://music.163.com/discover/playlist/?cat=%E8%8B%B1%E4%BC%A6'},
            {'金属': 'http://music.163.com/discover/playlist/?cat=%E9%87%91%E5%B1%9E'},
            {'朋克': 'http://music.163.com/discover/playlist/?cat=%E6%9C%8B%E5%85%8B'},
            {'蓝调': 'http://music.163.com/discover/playlist/?cat=%E8%93%9D%E8%B0%83'},
            {'雷鬼': 'http://music.163.com/discover/playlist/?cat=%E9%9B%B7%E9%AC%BC'},
            {'世界音乐': 'http://music.163.com/discover/playlist/?cat=%E4%B8%96%E7%95%8C%E9%9F%B3%E4%B9%90'},
            {'拉丁': 'http://music.163.com/discover/playlist/?cat=%E6%8B%89%E4%B8%81'},
            {'另类/独立': 'http://music.163.com/discover/playlist/?cat=%E5%8F%A6%E7%B1%BB%2F%E7%8B%AC%E7%AB%8B'},
            {'New Age': 'http://music.163.com/discover/playlist/?cat=New%20Age'},
            {'古风': 'http://music.163.com/discover/playlist/?cat=%E5%8F%A4%E9%A3%8E'},
            {'后摇': 'http://music.163.com/discover/playlist/?cat=%E5%90%8E%E6%91%87'},
            {'Bossa Nova': 'http://music.163.com/discover/playlist/?cat=Bossa%20Nova'},
            {'清晨': 'http://music.163.com/discover/playlist/?cat=%E6%B8%85%E6%99%A8'},
            {'夜晚': 'http://music.163.com/discover/playlist/?cat=%E5%A4%9C%E6%99%9A'},
            {'学习': 'http://music.163.com/discover/playlist/?cat=%E5%AD%A6%E4%B9%A0'},
            {'工作': 'http://music.163.com/discover/playlist/?cat=%E5%B7%A5%E4%BD%9C'},
            {'午休': 'http://music.163.com/discover/playlist/?cat=%E5%8D%88%E4%BC%91'},
            {'下午茶': 'http://music.163.com/discover/playlist/?cat=%E4%B8%8B%E5%8D%88%E8%8C%B6'},
            {'地铁': 'http://music.163.com/discover/playlist/?cat=%E5%9C%B0%E9%93%81'},
            {'驾车': 'http://music.163.com/discover/playlist/?cat=%E9%A9%BE%E8%BD%A6'},
            {'运动': 'http://music.163.com/discover/playlist/?cat=%E8%BF%90%E5%8A%A8'},
            {'旅行': 'http://music.163.com/discover/playlist/?cat=%E6%97%85%E8%A1%8C'},
            {'散步': 'http://music.163.com/discover/playlist/?cat=%E6%95%A3%E6%AD%A5'},
            {'酒吧': 'http://music.163.com/discover/playlist/?cat=%E9%85%92%E5%90%A7'},
            {'怀旧': 'http://music.163.com/discover/playlist/?cat=%E6%80%80%E6%97%A7'},
            {'清新': 'http://music.163.com/discover/playlist/?cat=%E6%B8%85%E6%96%B0'},
            {'浪漫': 'http://music.163.com/discover/playlist/?cat=%E6%B5%AA%E6%BC%AB'},
            {'性感': 'http://music.163.com/discover/playlist/?cat=%E6%80%A7%E6%84%9F'},
            {'伤感': 'http://music.163.com/discover/playlist/?cat=%E4%BC%A4%E6%84%9F'},
            {'治愈': 'http://music.163.com/discover/playlist/?cat=%E6%B2%BB%E6%84%88'},
            {'放松': 'http://music.163.com/discover/playlist/?cat=%E6%94%BE%E6%9D%BE'},
            {'孤独': 'http://music.163.com/discover/playlist/?cat=%E5%AD%A4%E7%8B%AC'},
            {'感动': 'http://music.163.com/discover/playlist/?cat=%E6%84%9F%E5%8A%A8'},
            {'兴奋': 'http://music.163.com/discover/playlist/?cat=%E5%85%B4%E5%A5%8B'},
            {'快乐': 'http://music.163.com/discover/playlist/?cat=%E5%BF%AB%E4%B9%90'},
            {'安静': 'http://music.163.com/discover/playlist/?cat=%E5%AE%89%E9%9D%99'},
            {'思念': 'http://music.163.com/discover/playlist/?cat=%E6%80%9D%E5%BF%B5'},
            {'影视原声': 'http://music.163.com/discover/playlist/?cat=%E5%BD%B1%E8%A7%86%E5%8E%9F%E5%A3%B0'},
            {'ACG': 'http://music.163.com/discover/playlist/?cat=ACG'},
            {'儿童': 'http://music.163.com/discover/playlist/?cat=%E5%84%BF%E7%AB%A5'},
            {'校园': 'http://music.163.com/discover/playlist/?cat=%E6%A0%A1%E5%9B%AD'},
            {'游戏': 'http://music.163.com/discover/playlist/?cat=%E6%B8%B8%E6%88%8F'},
            {'70后': 'http://music.163.com/discover/playlist/?cat=70%E5%90%8E'},
            {'80后': 'http://music.163.com/discover/playlist/?cat=80%E5%90%8E'},
            {'90后': 'http://music.163.com/discover/playlist/?cat=90%E5%90%8E'},
            {'网络歌曲': 'http://music.163.com/discover/playlist/?cat=%E7%BD%91%E7%BB%9C%E6%AD%8C%E6%9B%B2'},
            {'KTV': 'http://music.163.com/discover/playlist/?cat=KTV'},
            {'经典': 'http://music.163.com/discover/playlist/?cat=%E7%BB%8F%E5%85%B8'},
            {'翻唱': 'http://music.163.com/discover/playlist/?cat=%E7%BF%BB%E5%94%B1'},
            {'吉他': 'http://music.163.com/discover/playlist/?cat=%E5%90%89%E4%BB%96'},
            {'钢琴': 'http://music.163.com/discover/playlist/?cat=%E9%92%A2%E7%90%B4'},
            {'器乐': 'http://music.163.com/discover/playlist/?cat=%E5%99%A8%E4%B9%90'},
            {'榜单': 'http://music.163.com/discover/playlist/?cat=%E6%A6%9C%E5%8D%95'},
            {'00后': 'http://music.163.com/discover/playlist/?cat=00%E5%90%8E'}]

json = {
    'cate': '',
    'class': '',
    'url': '',
    'author': '',
    'create_time': '',
    'tags': '',
    'description': '',
    'transmit': '',
    'store': '',
    'comments': '',
    'played_times'
    'songs': [
        {
            'song_name': '',
            'time': '',
            'singer': '',
            'albunm': ''

        },
        {}
    ]
}
