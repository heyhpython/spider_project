# coding: utf-8 
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
cookie = 'anonymid=jhka681a-wqwe6y; depovince=GW; _r01_=1; JSESSIONID=abcR-pInaxZwX5gFfsrow; ick_login=599a271a-79fe-45eb-8c34-877657ed7a7a; first_login_flag=1; ln_uact=18842691265; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20130701/2235/h_main_JQK7_16e400002718113e.jpg; jebe_key=0925c9df-975d-44ee-9882-ae3c260f00ee%7C4955b9705d2c0415982e47c736dc93bf%7C1527150881269%7C1%7C1527150881189; _de=CD593955649036695EABF9B93F82E83E; jebecookies=de284dbb-0901-43bc-b063-5e7d838a0eb0|||||; p=6225398e02aaa8df542632339435e8a84; t=cc31c7442ad3178909f877b2bcffd6974; societyguester=cc31c7442ad3178909f877b2bcffd6974; id=424218344; xnsid=6e243b6d; loginfrom=syshome'

# 字典推导式
cookies = {i.split('=')[0]: i.split('=')[1] for i in cookie.split('; ')}
resp = requests.get('http://www.renren.com/424218344', headers=headers, cookies=cookies)
print(resp.content.decode())
