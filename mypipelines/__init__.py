# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MongoPipeline(object):
    def __init__(self):
        from pymongo import MongoClient
        from etc import config
        mongo = MongoClient(j=True, tz_aware=True, connect=False,
                            **config.mongodb_config)
        self._db = mongo[config.mongodb_dbname]
        self._index()

    def _index(self):
        from pymongo import ASCENDING
        self._db.user.create_index('uin', unique=True)
        self._db.clan.create_index('bid', unique=True)
        self._db.follow.create_index([('uin', ASCENDING), ('bid', ASCENDING)],
                                     unique=True)

    def process_item(self, item, spider):
        __type = item.pop('__type')
        if __type == 'user':
            self._db.user.replace_one({'uin': item['uin']}, item, upsert=True)
        elif __type == 'clan':
            self._db.clan.replace_one({'bid': item['bid']}, item, upsert=True)
        elif __type == 'follow':
            self._db.follow.replace_one(
                {'uin': item['uin'], 'bid': item['bid']}, item, upsert=True)
        else:
            raise TypeError('error type found: %s' % __type)
        return item
