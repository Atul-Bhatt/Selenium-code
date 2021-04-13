# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Tweet(Item):
    id_ = Field()
    raw_data = Field()


class User(Item):
    id_ = Field()
    raw_data = Field()
