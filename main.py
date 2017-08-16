# coding=utf-8
import douban
import json

id = 4746257

get_details = douban.Spider(id).get_details()
print json.dumps(get_details)