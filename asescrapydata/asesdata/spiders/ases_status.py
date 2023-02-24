from time import sleep
from scrapy.http import Response
import scrapy
from scrapy_splash import SplashRequest


class AsesStatusSpider(scrapy.Spider):
    name = "ases_status"
    allowed_domains = ["erros_avisos"]
    start_urls = ["https://asesweb.governoeletronico.gov.br/avaliar"]

    def start_requests(self):
        for url in self.start_urls:
            request = SplashRequest(url, method='POST', body='url=https%3A%2F%2Ftjro.jus.br',
                                     headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                     callback=self.parse_httpbin, args={'wait':10})
            yield request

    pass

    def parse_httpbin(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))

        for ases_data in response.css('#tabelaErros'):
            yield {
                'marcacao': ases_data.css('#tabelaErros tr:nth-child(1) .celula:nth-child(2)::text').get(),
                'comportamento': ases_data.css('tr:nth-child(2) .celula:nth-child(2)::text').get(),
                'conteudo_info': ases_data.css('tr:nth-child(3) .celula:nth-child(2)::text').get(),
                'apresentacao': ases_data.css('tr:nth-child(4) .celula:nth-child(2)::text').get(),
                'multimidia': ases_data.css('tr:nth-child(5) .celula:nth-child(2)::text').get(),
                'formularios': ases_data.css('tr:nth-child(6) .celula:nth-child(2)::text').get(),
                'total': ases_data.css('#total .topo:nth-child(2)::text').get()

            }

        print(response.text)

