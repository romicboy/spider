# coding=utf-8
import json

from station import ck, douban

douban_id = 26363254
ck_id = 27897
get_details = douban.Spider(douban_id).get_details()

details = ck.Spider(ck_id).get_details()

get_details['douban_id'] = douban_id
get_details['ck_id'] = ck_id
get_details['slides'] = details['slides']
get_details['links'] = details['links']

print json.dumps(get_details)