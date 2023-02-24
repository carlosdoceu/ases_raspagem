from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import scrapy
from scrapy.crawler import CrawlerProcess

from asescrapydata.asesdata.spiders.ases_status import AsesStatusSpider

chromedrive_path = 'C:/Users/504703/Documents/CODM/chrome_drive/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedrive_path)
sleep(2)
webdriver.get('https://asesweb.governoeletronico.gov.br/')

busca = webdriver.find_element(By.NAME, 'url')
busca.send_keys('www.tjro.jus.br/')

button_search = webdriver.find_element(By.CSS_SELECTOR, '#input_tab_1')
button_search.click()

ases_status_data = AsesStatusSpider(scrapy.Spider)
# process = CrawlerProcess(settings={'FEEDS': {'dados_ases.csv': {'formant': 'csv', }}})


#
# s = webdriver.page_source

ases_status_data.parse("https://www.google.com")

# process.crawl(AsesStatusSpider)
# process.start()

sleep(3)
