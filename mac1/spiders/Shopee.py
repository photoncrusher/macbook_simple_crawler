from ast import keyword
import scrapy
import json

class Shopee(scrapy.Spider):
    name = 'shopee'
    allowed_domains = ['shopee.vn']
    start_urls = ['https://{}/api/v4/search/search_items?by=relevancy&keyword={}&limit=60&newest={}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2'.format("shopee.vn", "macbook", 0)]
    lst_url = []

    def parse(self, response):
        item = dict()
        
        total_items = json.loads(response.text)["items"]
        for object in total_items:
            item[object["item_basic"]["name"]] = object["item_basic"]["price_before_discount"]
        # keyword = "macbook"
        # origin = "shopee.vn"
        # url = "https://{}/api/v4/search/search_items?by=relevancy&keyword={}&limit=60&newest={}&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"
        # for i in range(0, 2):
        #     new_url = url.format(keyword, origin, i*60)
        # for page_url in response.css('.cats-child-destop > li > a::attr(href)').extract():
        yield item

    # def parse_macbook(self, response):
    #     item = dict()
    #     item["name"] = "as"
    #     print("111111111111111111111111111")
        # item['name'] = response.css(
        #     '.header_content > h1 ::text').extract_first()

        # price = response.css(
        #     '.product-info-box > div > div > ins > .woocommerce-Price-amount::text ').extract_first()
        # if price == None:
        #     price = response.css(
        #         '.product-info-box > div > div  > .woocommerce-Price-amount > bdi::text ').extract_first()
        # item['price_sale'] = price
        # r_price = response.css(
        #     '.product-info-box > div > div > del > .woocommerce-Price-amount::text ').extract_first()
        # if r_price:
        #     item['price'] = r_price

        # lst_params = response.css(
        #     '#myModal12 > div > div  >  div.modal-body> table >tbody >tr')
        # for params in lst_params:
        #     if len(params.css('td::text')) > 1:
        #         params_name = params.css('td::text').extract_first().strip()
        #         params_value = params.css('td::text').extract()[1].strip()
        #         item[params_name] = params_value

        # item['url'] = url
        # item['website'] = self.allowed_domains[0]

        # yield item
