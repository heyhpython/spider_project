# coding: utf-8 
import requests

headers = {
    'Cookie': 'AD_RS_COOKIE=20080931; _trs_uv=jhohncd8_6_8fw5',
    'Referer': 'http://www.stats.gov.cn/tjsj/pcsj/rkpc/6rp/lefte.htm',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
url = 'http://www.stats.gov.cn/tjsj/pcsj/rkpc/6rp/excel/A0101d.xls'

resp = requests.get(url, headers=headers)
with open('xx.xls', 'wb') as f:
    f.write(resp.content)
