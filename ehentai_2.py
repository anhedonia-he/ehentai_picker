from bs4 import BeautifulSoup
import requests
import socket
import socks

def request(url):
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket
    # proxies = { "http": "http://127.0.0.1:1080", "https":'http://127.0.0.1:1080',}
    header = {
        'Referer':'http://g.e-hentai.org/',
        'Cookie':'eap_45442=1; ipb_member_id=3478845; ipb_pass_hash=5f44a298d72b120d278edbcf95ed95b1; ipb_session_id=1319b9d7b963ebcc42e95e862b3dac63; s=532b39fd8',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'
        }
    response = requests.get(url,headers = header)
    return response

url = 'http://g.e-hentai.org/g/1008601/42b1fb2e82/'
print('URL加载完成')
html = request(url)
print('requestget 完成')
soup = BeautifulSoup(html.text , 'lxml').find('div' , class_ = 'gdtm')
print(soup)
