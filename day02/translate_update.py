# coding: utf-8
import requests
import sys
import json


class BaiduTrans:
    '''百度翻译工具'''

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}

        self.url = 'http://fanyi.baidu.com/basetrans'

    def lang_dect(self, corpus):
        '''输入文本语言检测'''
        url = 'http://fanyi.baidu.com/langdetect'
        params = {'query': corpus}
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        resp = requests.post(url, params=params, headers=headers)
        lang = json.loads(resp.content.decode())['lan']
        return lang

    def set_params(self, corpus):
        source_lan = self.lang_dect(corpus)
        # 源语言是汉语
        data = {
            'query': corpus,
            'from': source_lan,
            'to': 'en' if source_lan == 'zh' else 'zh'
        }
        return data

    def translate(self, corpus):
        '''翻译的逻辑 参数sentence是要翻译的内容'''
        # 组织参数
        data = self.set_params(corpus)
        #  请求翻译
        resp = requests.post(self.url, data=data, headers=self.headers)
        # 接收返回数据
        data_json = resp.content.decode()
        data_dict = json.loads(data_json)
        print(data_dict['trans'][0]['result'][0][1])


if __name__ == '__main__':
    trans = BaiduTrans()
    # query = sys.argv[1]
    # 命令行输入可能不带引号的问题
    query = ' '.join(sys.argv[1:])
    trans.translate(query)


