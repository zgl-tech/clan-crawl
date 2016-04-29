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


def _parse_cookie(cookie_str):
    cookies = {}
    for item in cookie_str.split('; '):
        key, value = item.split('=', 1)
        cookies[key] = value
    return cookies


class ClanSpider(Spider):
    name = 'clan'
    start_urls = []

    def __init__(self, *largs, **kwargs):
        self._cookies = _parse_cookie(config.cookie_str)
        self._headers = config.headers
        super(ClanSpider, self).__init__(*largs, **kwargs)

    def _make_request(self, url, callback, meta=None):
        req = Request(url, cookies=self._cookies, headers=self._headers,
                      callback=callback)
        if meta:
            req.meta.update(meta)
        return req

    def start_requests(self):
        for uin in config.start_uins:
            url = _make_url(config.merge_top_url, targetuin=uin)
            yield self._make_request(url, self.parse_user, {'uin': uin})

    def parse_user(self, response):
        data = _parse_json(response.body_as_unicode())
        yield data['result']['userinfo']
        for followbar in data['result']['followbars']:
            yield followbar
        url = _make_url(config.fans_url, targetuin=response.meta['uin'],
                        start=0, num=config.fans_page_num)
        yield self._make_request(url, self.parse_fans,
                                 {'uin': response.meta['uin'], 'start': 0})

    def parse_fans(self, response):
        data = _parse_json(response.body_as_unicode())
        for follower in data['result']['follow_list']:
            url = _make_url(config.merge_top_url, targetuin=follower['uin'])
            yield self._make_request(url, self.parse_user,
                                     {'uin': follower['uin']})

        if len(data['result']['follow_list']) >= config.fans_page_num:
            return
        start = response.meta['start'] + config.fans_page_num
        url = _make_url(config.fans_url, targetuin=response.meta['uin'],
                        start=start, num=config.fans_page_num)
        yield self._make_request(url, self.parse_fans,
                                 {'uin': response.meta['uin'], 'start': start})
