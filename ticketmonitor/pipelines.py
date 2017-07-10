# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import subprocess


class TicketmonitorPipeline:
    def notify(self, spider):
        pass

    def process_item(self, item, spider):
        if item is not None:
            self.notify(spider)
        return item
