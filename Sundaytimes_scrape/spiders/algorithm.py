import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'http://www.sundaytimes.lk/news/',
        'http://www.sundaytimes.lk/news/10',
        'http://www.sundaytimes.lk/news/20',
        'http://www.sundaytimes.lk/news/30',
        'http://www.sundaytimes.lk/news/40',
        'http://www.sundaytimes.lk/news/50',
        'http://www.sundaytimes.lk/news/60',
        'http://www.sundaytimes.lk/news/70',
        'http://www.sundaytimes.lk/news/80',
        'http://www.sundaytimes.lk/news/90',
        'http://www.sundaytimes.lk/business/',
        'http://www.sundaytimes.lk/business/10',
        'http://www.sundaytimes.lk/business/20',
        'http://www.sundaytimes.lk/business/30',
        'http://www.sundaytimes.lk/business/40',
        'http://www.sundaytimes.lk/business/50',
        'http://www.sundaytimes.lk/business/60',
        'http://www.sundaytimes.lk/business/70',
        'http://www.sundaytimes.lk/business/80',
        'http://www.sundaytimes.lk/business/90',
        'http://www.sundaytimes.lk/world/',
        'http://www.sundaytimes.lk/world/10',
        'http://www.sundaytimes.lk/world/20',
        'http://www.sundaytimes.lk/world/30',
        'http://www.sundaytimes.lk/world/40',
        'http://www.sundaytimes.lk/world/50',
        'http://www.sundaytimes.lk/world/60',
        'http://www.sundaytimes.lk/world/70',
        'http://www.sundaytimes.lk/world/80',
        'http://www.sundaytimes.lk/world/90',
        'http://www.sundaytimes.lk/sport',
        'http://www.sundaytimes.lk/sport/10',
        'http://www.sundaytimes.lk/sport/20',
        'http://www.sundaytimes.lk/sport/30',
        'http://www.sundaytimes.lk/sport/40',
        'http://www.sundaytimes.lk/sport/50',
        'http://www.sundaytimes.lk/sport/60',
        'http://www.sundaytimes.lk/sport/70',
        'http://www.sundaytimes.lk/sport/80',
        'http://www.sundaytimes.lk/sport/90',

    ]

    def parse(self, response):
        for news in response.css('div.cat-zero'):
            yield {
                'title': news.css('h1.cat-header::text').extract(),
                'newsitem': news.css('p.cat-text::text').extract(),
                'date': news.css('p.cat-other span::text').extract(),
                'comments' : news.css('p.cat-other strong::text').extract()
            }
