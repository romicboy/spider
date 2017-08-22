# coding=utf-8

class Item:

    # 详情地址
    url_item = 'https://baike.baidu.com/item/{}'

    def get_url(self, name):
        return self.url_item.format(name)