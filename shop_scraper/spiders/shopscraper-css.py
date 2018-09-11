from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from shop_scraper.items import BottomsScraperItem, ExclusiveScraperItem
from w3lib.html import remove_tags, replace_escape_chars, strip_html5_whitespace


class BottomScraperCss(CrawlSpider):
    name = 'bottomscraper-css'
    start_urls = ['https://suzyshier.com/collections/sz_bottoms_shop-all-bottoms']

    rules = (
        Rule(LinkExtractor(restrict_css=".featured-collection__info.js-product-tile > a"), callback="parse_shop", follow=True),
    )

    def parse_shop(self, response):
        shop_loader = ItemLoader(item=BottomsScraperItem(), response=response)
        shop_loader.default_input_processor = MapCompose(remove_tags, replace_escape_chars, strip_html5_whitespace)
        shop_loader.default_output_processor = TakeFirst()

        shop_loader.add_css("title", ".grid__item.large-up--one-third.product__selector-container > h1")
        shop_loader.add_css("price", "span.product__price.js-product-price")
        shop_loader.add_css("color", ".product__option-label.product__option-label > span")
        shop_loader.add_css("sizes", ".product__radio-size-text")
        shop_loader.add_css("specs", "#toggle-product__specs > ul")
        shop_loader.add_css("description", "#toggle-product__description")
        yield shop_loader.load_item()


class ExclusiveScraperCss(CrawlSpider):
    name = 'exclusivescraper-css'
    start_urls = ['https://suzyshier.com/collections/sz_trend_online-exclusives']

    rules = (
        Rule(LinkExtractor(restrict_css=".featured-collection__info.js-product-tile > a"), callback="parse_shop", follow=True),
    )

    def parse_shop(self, response):
        shop_loader = ItemLoader(item=ExclusiveScraperItem(), response=response)
        shop_loader.default_input_processor = MapCompose(remove_tags, replace_escape_chars, strip_html5_whitespace)
        shop_loader.default_output_processor = TakeFirst()

        shop_loader.add_css("title", ".grid__item.large-up--one-third.product__selector-container > h1")
        shop_loader.add_css("price", "span.product__price.js-product-price")
        shop_loader.add_css("discount_price", "span.product__price.product__discount.js-product-price")
        yield shop_loader.load_item()