#作业就是读取到响应内容 然后提取出“发送成功”和发送的信息 提示：使用json模块能将字符串转换成字典
from urllib import  request,parse
import http.cookiejar
import gzip
import json
def crawler():
    message = str(input('请输入你的评论:'))
    url = ' https://api.bilibili.com/x/v2/reply/add'
    form_data = {
        'oid': '540379650',
        'type': '1',
        'message': message,
        'plat': '1',
        'jsonp': 'jsonp',
        'csrf': '2465bf0f43863f1f72da4437e8a3f7f7'
    }
    data = bytes(parse.urlencode(form_data),encoding='utf-8')
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Host": "api.bilibili.com",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://www.bilibili.com",
        "Referer": "https://www.bilibili.com/video/BV1ii4y1t7Ri?from=search&seid=13227842417220944957",
        "Cookie":"_uuid=6545DCA1-06AD-4CC5-DAEE-66A47A079FB968566infoc; buvid3=FB65770C-8357-41F6-B780-8B395463BE9253923infoc; sid=lfvz8p4k; DedeUserID=452320745; DedeUserID__ckMd5=d305967df50bec7c; SESSDATA=c722af0c%2C1602934275%2C4c34d*41; bili_jct=2465bf0f43863f1f72da4437e8a3f7f7; CURRENT_FNVAL=16; LIVE_BUVID=AUTO1815873823108358; rpdid=|(J|)R)|~R|J0J'ul)~J)kJ|m; CURRENT_QUALITY=64; bfe_id=393becc67cde8e85697ff111d724b3c8; PVID=1"
    }
    #构建requests对象
    requests = request.Request(url=url,headers=headers,data=data)
    #CookieJar 类储存 HTTP cookies。它从 HTTP 请求提取 cookies，并在 HTTP 响应中返回它们。
    cookie = http.cookiejar.CookieJar()
    #request.HTTPCookieProcessor用于处理 HTTP Cookies
    handler = request.HTTPCookieProcessor(cookie)
    #request.build_opener返回一个OpenerDirector实例，该实例按给定的顺序链接处理程序
    opener = request.build_opener(handler)
    response = opener.open(requests)
    #GzipFile 类可以读写 gzip 格式的文件，还能自动压缩和解压缩数据,此处用的是gzip 格式，所以要调用次方法来读数据
    response = gzip.GzipFile(fileobj=response)
    #转化成字典
    response = json.loads(response.read())
    print(response['data']['success_toast'])
crawler()