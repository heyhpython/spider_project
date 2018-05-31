# coding: utf-8 
import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
    "Referer": "https://m.douban.com/movie/nowintheater?loc_id=108288"
}


@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data, proxies):
    '''请求url'''
    if method == 'get':
        html= requests.get(url, headers=headers, proxies=proxies, data=data, verify=False)
    elif method == 'post':
        html = requests.post(url, headers=headers, proxies=proxies, data=data, verify=False)
    html.encoding = 'utf-8'
    return html.text


def parse_url(url, method="get", data={}, proxies={}):
    '''参数的格式化'''
    try:
        html_str = _parse_url(url, method, data, proxies)
    except Exception as e:
        print(e)
        html_str = None
    return html_str


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(parse_url(url))