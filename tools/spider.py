# coding=utf-8
import urllib2
from bs4 import BeautifulSoup

class Spider:

    def get_soup(self, url):
        # httpHandler = urllib2.HTTPHandler(debuglevel=1)
        # httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
        # opener = urllib2.build_opener(httpHandler, httpsHandler)
        # urllib2.install_opener(opener)

        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return BeautifulSoup(response)

    def get_response(self, url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()