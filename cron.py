# -*- coding:utf-8 -*-

import json
import redis
import logging
import time

from station import douban, ck


def cron():

    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] "%(module)s" %(message)s')
    redisClient = redis.Redis(host='10.211.55.7', port=6379, db=0)
    sleepSecond = 60
    queueName = 'spider-job-moive'

    while True:

        jobJson = redisClient.lpop(queueName)

        if jobJson is None:
            logging.info('queue is empty, sleep %s seconds', sleepSecond)
            time.sleep(sleepSecond)
            continue

        logging.info('jobJson : %s', jobJson)

        job = json.loads(jobJson)
        douban_id = job['douban_id']
        ck_id = job['ck_id']

        get_details = douban.Spider(douban_id).get_details()
        details = ck.Spider(ck_id).get_details()

        get_details['douban_id'] = douban_id
        get_details['ck_id'] = ck_id
        get_details['slides'] = details['slides']
        get_details['links'] = details['links']

        print json.dumps(get_details)


if __name__ == '__main__':
    cron()
