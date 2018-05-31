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

    def set_params(self, sentence):
        data = {
            'query': sentence,
            'from': 'zh',
            'to': 'en'
        }
        return data

    def lang_dect(self):
        '''输入文本语言检测'''
        url = 'http://fanyi.baidu.com/langdetect'
        params = {'query': 'hello'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        resp = requests.post(url, params=params)
        lang = json.loads(resp.content.decode())['lan']
        return lang

    def translate(self, sentence):
        # sentence = input('输入内容')
        data = self.set_params(sentence)
        resp = requests.post(self.url, data=data, headers=self.headers)
        data_json = resp.content.decode()
        data_dict = json.loads(data_json)
        print(data_dict['trans'][0]['result'][0][1])

# todo 识别语种 汉语翻译成英文 非汉语翻译成汉语
if __name__ == '__main__':
    trans = BaiduTrans()
    query = sys.argv[1]
    trans.translate(query)

# {'trans': [{'relation': [], 'result': [[0, 'Hello', ['0|6'], [], ['0|6'], ['0|5']]], 'prefixWrap': 0, 'src': '你好',
#             'dst': 'Hello'}], 'errno': 0, 'dict': {'word_name': '你好', 'word_means': ['hello', 'hi', 'How do you do!'],
#                                                    'symbols': [{'symbol_mp3': '', 'word_symbol': 'nǐ hǎo', 'parts': [
#                                                        {'part_name': '', 'means': [
#                                                            {'has_mean': 1, 'word_mean': 'hello', 'text': 'hello',
#                                                             'split': '1', 'means': ['打招呼', '哈喽，喂', '你好，您好', '表示问候'],
#                                                             'part': 'int.'},
#                                                            {'has_mean': 1, 'word_mean': 'hi', 'text': 'hi',
#                                                             'split': '1', 'means': ['（用作问候语）嘿，喂'], 'part': 'int.'},
#                                                            {'has_mean': 1, 'word_mean': 'How do you do!',
#                                                             'text': 'How do you do!', 'split': '0', 'means': ['你好！'],
#                                                             'part': 'st.'}]}]}], 'items': [''], 'from': 'kingsoft',
#                                                    'is_CRI': 0},
#  'en_ph': {'ph_am': 'həˈloʊ', 'ph_en': "hə'ləʊ", 'ph_en_mp3': '', 'ph_other': '',
#            'ph_am_mp3': '/1/0/5d/41/5d41402abc4b2a76b9719d911017c592.mp3',
#            'ph_tts_mp3': '/5/d/4/5d41402abc4b2a76b9719d911017c592.mp3'}, 'to': 'en', 'from': 'zh'}
