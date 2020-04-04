"""casinoenlineahex spider"""
import scrapy


class CasinoenlineahexSpider(scrapy.Spider):
    """casinoenlineahex spider"""

    name = "casinoenlineahex"

    def start_requests(self):
        url = "https://casinoenlineahex.com/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.css("div[id*=casinos] table tbody tr"):
            yield {
                "id": row.css("td.col-0 span::text").extract_first(),
                "name": row.css("td.col-4 a span::text").extract_first(),
                "bonuses": row.css("td.col-5 span::text").extract_first(),
                "payments": row.css("td.col-6 ul li img::attr(title)").getall(),
            }
