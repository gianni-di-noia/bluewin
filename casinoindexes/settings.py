"""
Scrapy settings for casinoindexes project
For simplicity, this file contains only settings considered important or
commonly used. You can find more settings consulting the documentation:
    https://doc.scrapy.org/en/latest/topics/settings.html
    https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
    https://doc.scrapy.org/en/latest/topics/spider-middleware.html
"""

BOT_NAME = "casinoindexes"

SPIDER_MODULES = ["casinoindexes.spiders"]
NEWSPIDER_MODULE = "casinoindexes.spiders"

ROBOTSTXT_OBEY = True

MONGO_URI = "mongodb://admin:admin@mongodb:27017"
MONGO_DATABASE = "bluewindow"

ITEM_PIPELINES = {
    "casinoindexes.pipelines.MongoPipeline": 300,
}
