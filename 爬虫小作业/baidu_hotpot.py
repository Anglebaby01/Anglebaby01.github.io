import requests
import re
from lxml import etree
def crawler():
    url = 'http://top.baidu.com/category?c=513&fr=topbuzz_b1_c513'
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)

    response.encoding = response.apparent_encoding
    #print(response.encoding)
    html = response.text
    #print(response.text)
    #pattern = re.compile('<td>\s<class"keyword">\s+<a.*?>(.*?)</a>')
    #data = re.findall(pattern,response)
    html= etree.HTML(html)
    #for i in range(1,10):
    result = html.xpath('//*[@id="main"]/div[3]/div[2]/div/div/div/ul/li/div[1]/a[1]/text()')
    index = 0
    print("         今日热点")
    for i in result:
        index += 1
        print(index," ,",i)

crawler()