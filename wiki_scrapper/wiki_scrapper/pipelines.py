# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exceptions import DropItem
from datetime import datetime

class WikiScrapperPipeline:
    def process_item(self, item, spider):
        return item

class CheckValue:
    def process_item(self, article, spider):

        if not article['lastUpdated'] or not article['url']: # or not article['title']:
            raise DropItem('Missing data')
        return article
    
class CleanDatePipeline:
    def process_item(self, article,spider):
        cleaned_last_updated = article['lastUpdated'].replace("This page was last edited on", "").strip()
        # print("\n\n\n\n\n\n\ncleaning")
        article['lastUpdated'] = datetime.strptime(cleaned_last_updated, '%d %B %Y, at %H:%M')
        return article