import re
import json
import logging
from urllib.parse import quote  # make data safe for use as URL

from scrapy import http  # to generate a request
from scrapy.spiders import CrawlSpider
# to check if you got the correct response
from scrapy.shell import inspect_response
from scrapy.core.downloader.middleware import DownloaderMiddlewareManager
'''
The downloader middleware is a framework of hooks into Scrapy's request/response processing.
It's a light, low-level system for globally altering Scrapy's requests and responses.
'''
from scrapy_selenium import SeleniumRequest, SeleniumMiddleware

from tweetcrawler.items import Tweet, User

logger = logging.getLogger(__name__)


class TweetScraper(CrawlSpider):
    name = 'tweetcrawler'
    allowed_domains = ["twitter.com"]

    def __init__(self, query=''):
        self.url = (
            f'https://api.twitter.com/2/search/adaptive.json?'
            f'include_profile_interstitial_type=1'
            f'&include_blocking=1'
            f'&include_blocked_by=1'
            f'&include_followed_by=1'
            f'&include_want_retweets=1'
            f'&include_mute_edge=1'
            f'&include_can_dm=1'
            f'&include_can_media_tag=1'
            f'&skip_status=1'
            f'&cards_platform=Web-12'
            f'&include_cards=1'
            f'&include_ext_alt_text=true'
            f'&include_quote_count=true'
            f'&include_reply_count=1'
            f'&tweet_mode=extended'
            f'&include_entities=true'
            f'&include_user_entities=true'
            f'&include_ext_media_color=true'
            f'&include_ext_media_availability=true'
            f'&send_error_codes=true'
            f'&simple_quoted_tweet=true'
            f'&query_source=typed_query'
            f'&pc=1'
            f'&spelling_corrections=1'
            f'&ext=mediaStats%2ChighlightedLabel'
            f'&count=20'
            f'&tweet_search_mode=live'
        )
        self.url = self.url + '&q={query}'
        self.query = query
        self.num_search_issued = 0
        # regex for finding next cursor
        self.cursor_re = re.compile('"(scroll:[^"]*)"')

    def start_requests(self):
        '''
        Use landing page to get cookies first
        '''
        yield SeleniumRequest(url="https://twitter.com/explore", callback=self.parse_home_page)
