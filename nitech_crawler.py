# -*- coding = utf-8 -*-
# @Time : 2021/04/10 16:00
# @File : nitech_crawler.py
# @Softeware : PyCharm

import requests
from lxml import etree
import os
# import ssl

if not os.path.exists('./nitech_news'):
    os.mkdir('./nitech_news')
# ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    # 'Connection': 'close'
}
url_base = 'https://www.nitech.ac.jp/news/'

s = requests.session()

with open('./nitech_news/nitech_news.txt', 'w', encoding='utf-8') as fp:
    #crawl page 1
    response = s.get(url=url_base, headers=headers, verify=False)
    response.encoding = 'utf-8'
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)

    a_list = tree.xpath('//div[@id="main"]/div[@id="news-kasou-list"]/article')

    for news in a_list:
        news_time = news.xpath('./time/text()')[0]
        news_title = news.xpath('./p[@class="news-title"]/a/text()')[0]

        fp.write(news_time + "\b" + news_title + "\n")
        print(news_time, "\b", news_title)

    #crawl page 2-167
    for i in range(2, 168):
        url = url_base + 'index_' + str(i) + '.html'
        response = s.get(url=url, headers=headers, verify=False)
        response.encoding = 'utf-8'
        page_text = response.text
        tree = etree.HTML(page_text)
        a_list = tree.xpath('//div[@id="main"]/div[@id="news-kasou-list"]/article')

        for news in a_list:
            news_time = news.xpath('./time/text()')[0]
            news_title = news.xpath('./p[@class="news-title"]/a/text()')[0]

            fp.write(news_time + "\b" + news_title + "\n")
            print(news_time, "\b", news_title)
