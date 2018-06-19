import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'http://www.sundaytimes.lk/news/',
        'http://www.sundaytimes.lk/news/10',
        'http://www.sundaytimes.lk/news/20',
        'http://www.sundaytimes.lk/news/30',
        'http://www.sundaytimes.lk/news/40',
    ]

    def parse(self, response):
        for news in response.css('div.cat-zero'):
            yield {
                'title': news.css('h1.cat-header::text').extract(),
                'newsitem': news.css('p.cat-text::text').extract(),
                'date': news.css('p.cat-other span::text').extract(),
                'comments' : news.css('p.cat-other strong::text').extract()
            }
