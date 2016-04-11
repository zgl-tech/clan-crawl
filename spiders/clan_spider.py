#  coding: utf-8

from scrapy import Spider, Request
import simplejson as json
from urllib import urlencode

from etc import config


def _make_url(url, **query):
    return '%s?%s' % (url, urlencode(query))


def _parse_json(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise RuntimeError(u'body error: %s' % text)


class ClanSpider(Spider):
    name = 'clan'
    start_urls = []

    def start_requests(self):
        for uin in config.start_uins:
            url = _make_url(config.merge_top_url, targetuin=uin)
            req = Request(url, cookies=config.cookies, headers=config.headers,
                          callback=self.parse_user)
            req.meta['uin'] = uin
            yield req

    def parse_user(self, response):
        data = _parse_json(response.body_as_unicode())
        yield data['result']['userinfo']
        for followbar in data['result']['followbars']:
            yield followbar
        url = _make_url(config.fans_url, targetuin=response.meta['uin'],
                        start=0, num=config.fans_page_num)
        req = Request(url, cookies=config.cookies, headers=config.headers,
                      callback=self.parse_fans)
        req.meta['uin'] = response.meta['uin']
        req.meta['start'] = 0
        yield req

    def parse_fans(self, response):
        data = _parse_json(response.body_as_unicode())
        for follower in data['result']['follow_list']:
            url = _make_url(config.merge_top_url, targetuin=follower['uin'])
            req = Request(url, cookies=config.cookies, headers=config.headers,
                          callback=self.parse_user)
            req.meta['uin'] = follower['uin']
            yield req

        if len(data['result']['follow_list']) >= config.fans_page_num:
            return
        start = response.meta['start'] + config.fans_page_num
        url = _make_url(config.fans_url, targetuin=response.meta['uin'],
                        start=start, num=config.fans_page_num)
        req = Request(url, cookies=config.cookies, headers=config.headers,
                      callback=self.parse_fans)
        req.meta['uin'] = response.meta['uin']
        req.meta['start'] = start
        yield req
