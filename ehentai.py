from bs4 import BeautifulSoup
import requests
import socket
import socks
import os

class ehentai():

    def request(self , url):
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

    def mkdir(self , path):
        front_pass = "/Users/Anhedonia/Desktop/存储/本子/"
        isExists = os.path.exists(os.path.join(front_pass, path))

        if not isExists:
            os.makedirs(os.path.join(front_pass,path))
            os.chdir(front_pass+'/'+path)
        else:
            os.chdir(front_pass+'/'+path)

    def save(self , img_url , img):
        name = img_url[-7:-4]
        f = open(name+'.jpg', 'ab')
        f.write(img.content)
        f.close()

    def main(self , url):
        html = self.request(url)
        print('requestget 完成')
        img_soup_list = BeautifulSoup(html.text , 'lxml').find_all('div' , class_ = 'gdtm')
        path = BeautifulSoup(html.text , 'lxml').h1.string
        for img_html in img_soup_list:
            imgview_url = img_html.find('a')['href']
            imgview = self.request(imgview_url)
            img_url = BeautifulSoup(imgview.text , 'lxml').find('div',id='i3').find('img')['src']
            img = self.request(img_url)
            self.mkdir(path)
            self.save(img_url , img)

ehentai_picker = ehentai()
ehentai_picker.main('http://g.e-hentai.org/g/1008601/42b1fb2e82/')
