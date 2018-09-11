import scrapy


class BottomsScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    sizes = scrapy.Field()
    specs = scrapy.Field()
    description = scrapy.Field()
    pass


class ExclusiveScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    discount_price = scrapy.Field()