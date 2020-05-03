import requests
from lxml import etree

class Crawler():
    def __init__(self):
        self.BASE_URL = "https://bing.ioliu.cn"
        self.TOTAL_PAGE = 124
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        }

    def spider(self):
        session = requests.Session()
        for index in range(1 ,self.TOTAL_PAGE+1):
            url = self.BASE_URL + f"/?p={index}"
            response = session.get(url=url, headers=self.headers)
            yield response.content.decode("utf8")

    @staticmethod
    def parser(html):
        selector = etree.HTML(html)
        url_list = selector.xpath("//div[@class='item']//div[@class='options']/a[2]/@href")
        return url_list

    def save_picture(self, url_list):
        session = requests.Session()
        index = 0
        for url in url_list:
            index += 1
            file_name = url.split("/")[2][:-15] + ".jpg"
            picture_url =  self.BASE_URL + url
            response = session.get(picture_url, headers=self.headers)
            with open(file_name, "wb") as file:
                file.write(response.content)
                print('photo',index,':save successfully')

    def run(self):
        html_gen = self.spider()
        for html in html_gen:
            url_list = self.parser(html)
            self.save_picture(url_list)

if __name__ == '__main__':
    bing_spider = Crawler()
    bing_spider.run()