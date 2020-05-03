# -*- coding:utf-8 -*-
import requests
from lxml import etree

class XlsDownload:
    def __init__(self):
        self.url = 'http://jw.cdu.edu.cn/Infors/Business.aspx?classID=1'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Cookie': 'UM_distinctid=171d93a82d573-0c7aa05d6fe476-c373667-1fa400-171d93a82d63a2; ASP.NET_SessionId=xdqzilhygy3fgnryrhsrhkge',
            'Referer': 'http://jw.cdu.edu.cn/Infors/Business.aspx?classID=2',
            'Host': 'jw.cdu.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36',
            'Upgrade-Insecure-Requests': '1'
        }

    #找表
    def findXls(self):
        response = requests.get(url=self.url,headers=self.headers)
        html = etree.HTML(response.text)
        xls_name = html.xpath('//div/div/li/ui/li')

        print(xls_name)
        print(response.text)
        pass


    #存表
    def saveXls(self):
        pass

    def main(self):
        pass
if __name__ == '__main__':
    xls = XlsDownload()
    xls.findXls()