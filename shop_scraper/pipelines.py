from scrapy.exporters import JsonItemExporter


class BottomScraperPipeline():
    def __init__(self):
        self.file = open("data/data_shop.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        #if isinstance(item, BottomsScraperItem):
        self.exporter.export_item(item)
        return item


class ExclusiveScraperPipeline():
    def __init__(self):
        self.file = open("data/data_shop.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        #if isinstance(item, ExclusiveScraperItem):
        self.exporter.export_item(item)
        return item