# coding=utf-8
import spider
import json

class Info():

    url_item = 'http://www.ck180.net/{0}.html'

    def get_url(self, id):
        return self.url_item.format(id)


    def get_slides(self, soup):
        imgs = soup.select("ul.slides li img")

        result = []
        for img in imgs:
            src = img.attrs['src']
            result.append(src[0:len(src)-6])
        return result


class Download():
    url_item = 'http://api.hzxdr.cn/api/json_{0}.json'

    def get_url(self, id):
        return self.url_item.format(id)

    def get_links(self, url):
        response = spider.Spider().get_response(url)
        return json.loads(response[1:len(response) - 1])

class Spider:

    id = None
    info = Info()
    download = Download()

    def __init__(self, id):
        self.id = id

    def get_details(self):

        details = {}

        info_soup = spider.Spider().get_soup(self.info.get_url(self.id))
        details['slides'] = self.info.get_slides(info_soup)
        details['links'] = self.download.get_links(self.download.get_url(self.id))

        return details