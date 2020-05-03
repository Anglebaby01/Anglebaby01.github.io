# -*- coding: utf-8 -*-
import requests
from lxml import etree
from requests.exceptions import RequestException
import csv

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '_zap=4d320cf8-0e44-493b-94db-8d14249f5bd4; _xsrf=SiZUHNPtPiGlRvc6sCj2Lid9CBHms7OF; d_c0="AFAkcy9vKg6PTrQV_SzCZMkrvvcsSbDM0Gw=|1536145887"; q_c1=7b6c590408af44b8b4b1f5ae142a24a2|1536146175000|1536146175000; tgw_l7_route=69f52e0ac392bb43ffb22fc18a173ee6; capsion_ticket="2|1:0|10:1536152892|14:capsion_ticket|44:NjcyYWE2ZDQ1MDViNGVjZjhkZTYwOTJhNzg3ZTJmMmQ=|c2a0f151bc07388cba8fade0dda7a29a9ada1d50a664398ea4bbb14cf2eedc47"; z_c0="2|1:0|10:1536152899|4:z_c0|92:Mi4xbGxDLUJ3QUFBQUFBVUNSekwyOHFEaVlBQUFCZ0FsVk5ReU45WEFBMWdWcUxrVTRMcXAxR0hUMmM4am80NFYyd1hB|6047e629d40ce5791cc0430b2733a5dc767e46b0fd85ed36485cf0f9c92eaa8d"',
    'referer': 'https://www.zhihu.com/pub/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'x-requested-with': 'Fetch'
}


def parse_html(data):
    # jsondata=json
    # print(data)

    itemsinfo = data['data']

    for pinfo in itemsinfo:
        # print(pinfo)
        id = pinfo['id']
        des = pinfo['description']
        title = pinfo['title']
        url = pinfo['url']
        book_size = pinfo['book_size']
        score = pinfo['score']
        picture = pinfo['cover']

        authors_name = []
        for author in pinfo['authors']:
            author_name = author['name']
            authors_name.append(author_name)
        # print(authors_name)

        price = pinfo['promotion']['price']
        # print(price)
        yield {
            "ID": id,
            "描述": des,
            "标题": title,
            "地址": url,
            "书本字数": book_size,
            "评分": score,
            "图片": picture,
            "作者": authors_name,
            "价格": price,

        }

#获取资源
def get_html(url):
    try:
        req = requests.get(url, headers=headers)

        if req.status_code == 200:
            # print("******")
            return req.json()
        return None
    except RequestException as e:
        return None

#保存
def write_csv_header(file, headers):
    with open(file, 'a', encoding='utf-8', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()


def write_csv_rows(path, headers, rows):
    with open(path, 'a', encoding='utf-8', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writerows(rows)


def main():
    filename = "知乎书店.csv"
    headers = ['ID', '描述', '标题', '地址', '书本字数', '评分', '图片', '作者', '价格']
    write_csv_header(filename, headers)

    for book in range(5, 100, 5):
        books = []
        base_url = "https://www.zhihu.com/api/v3/books/categories/147?version=v2&limit=5&sort_by=read_count_7days&offset={}".format(
            book)
        # print(base_url)
        content = get_html(base_url)
        # print(content)
        items = parse_html(content)
        # print(items)
        for item in items:
            books.append(item)
        write_csv_rows(filename, headers, books)
if __name__ == '__main__':
    print('正在下载中~')
    main()
    print('下载完成~')