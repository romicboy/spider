# coding=utf-8
import collections
import spider

class Info():

    # 详情地址
    url_item = 'https://movie.douban.com/subject/{0}/'

    def get_url(self, id):
        return self.url_item.format(id)

    # 评分
    def get_rating_num(self,soup):
        var = soup.find_all("strong", class_="ll rating_num")[0]
        return var.string

    # 电影名称
    def get_name(self, soup):
        content = soup.select('.lnk-sharing')[0].attrs['data-name']
        return content

    # 剧情简介
    def get_report(self, soup):
        content = None
        report = soup.select('#link-report .all')
        if len(report) > 0 :
            content = report[0].text.strip()
        else :
            content = soup.select('#link-report span')[0].text.strip()
        return content

    def get_info(self, soup):
        content = soup.select('#info')[0]
        list = []
        for info in content:
            text = None
            if hasattr(info, 'text'):
                text = info.text
            else:
                text = info

            text = text.strip()

            if text != '':
                list.append(text)

        result = []
        for i in range(0, len(list)-1):
            item = list[i]

            if item.find(":") != -1:
                result.append(item)
            else:
                result[len(result)-1] += item

        dic = collections.OrderedDict()
        for item in result:
            arr = item.split(":")
            dic[arr[0].strip()] = arr[1].strip()

        return dic

class Playbill:

    # 海报地址
    url_playbill = 'https://movie.douban.com/subject/{0}/photos?type=R&start=0&sortby=like&size=a&subtype=o'

    url_photo = 'https://movie.douban.com/photos/photo/{0}/'

    url_photo_image = 'https://img1.doubanio.com/view/photo/photo/public/p{0}.jpg'

    def get_url(self, id):
        return self.url_playbill.format(id)

    def get_photo_url(self, id):
        return self.url_photo.format(id)

    # 海报图片id集合
    def get_photo_ids(self, soup):
        result = []
        lis = soup.select('ul.poster-col4 li')
        for li in lis:

            if li.has_key('data-id'):
                result.append(li.attrs['data-id'])
        return result


    def get_photo_image(self, id):
        return self.url_photo_image.format(id)

    def get_photo_images(self, photo_ids):
        list = []
        for id in photo_ids:
            list.append(self.url_photo_image.format(id))

        return list


class Spider:

    id = None
    info = Info()
    playbill = Playbill()

    def __init__(self, id):
        self.id = id

    def get_details(self):

        details = {}
        info_soup = spider.Spider().get_soup(self.info.get_url(self.id))

        details['name'] = self.info.get_name(info_soup)
        details['info'] = self.info.get_info(info_soup)
        details['report'] = self.info.get_report(info_soup)
        details['rating_num'] = self.info.get_rating_num(info_soup)

        playbill_soup = spider.Spider().get_soup(self.playbill.get_url(self.id))
        photo_ids = self.playbill.get_photo_ids(playbill_soup)
        details['photo_ids'] = photo_ids
        details['photo_images'] = self.playbill.get_photo_images(photo_ids)

        return details