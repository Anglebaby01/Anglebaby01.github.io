### 二、urllib库简介
+ urllib是Python内置的一个HTTP请求库
+ 包含4个模块：request,error,parse,robotparser
#### 1.urllib.request
+ 模拟浏览器像服务器发送请求，需要使用的是urllib.request模块，其中最基础的请求方法就是 urlopen() 方法,默认为GET请求，传入data后为POST请求
    ```
    urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None,cadefault=False,context=None) 
    ```
    + url 可以是字符串，也可以是自己构造的Request对象
    + data 是需要发送给服务器的数据对象，如果没有则不用填写， 默认为None
    + timeout 超时设置，是一个可选参数，传入超时时间后，如果在指定的时间内服务器没有响应则抛出 timeout 异常，基本上爬虫时都会用到，以避免服务器未响应
    + cafile 和 capath 代表 CA 证书和 CA 证书的路径。如果使用 HTTPS 则可能需要用到
    + context 参数必须是 ssl.SSLContext 类型，用来指定 SSL 设置
+ 请求网页
    ``` 
        import urllib.request  """导入模块"""

        url = "http://www.baidu.com"
        response = urllib.request.urlopen(url)  #使用 urlopen 方法获取到的是一个 http.client.HTTPResponse 对象
        html = response.read()   #使用 read() 方法将response中的网页源代码读出来
        print(html.decode('utf-8'))  #使用 decode() 方法将读取出来的网页源代码编码转换成 utf-8 编码
    ```
    + 其他的一些操作：
        + response.getcode()，获取状态码
        + response.readline()，以字节流 返回所有得数据 以列表格式保存
        + response.getheaders()，获取响应头
        + response.geturl()，获取url      
              ------   
+ 构建Request对象
    + urlopen() 可以支撑我们的一些简单的请求，但是请记住，一个没有请求头的爬虫是没有灵魂的。虽然不使用请求头也可以访问一些网页，但是这样的行为是直接告诉服务器“我是一个爬虫”，那么服务器可能就会拒绝程序的请求，因此我们需要进行伪装，这时候我们就需要去构造我们的HTTP请求体，一个Request对象。
    ```
    import urllib.request
    def crawler():
        url = "http://www.maoyan.com"
        headers = {
        "User-agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50
        (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }

        request = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(request)
        print(response.read().decode('utf-8'))
    
    crawler()
    ```
   


#### 2.urllib.parse
+ 用于解析URL（python由ASCII编码，不支持中文，输入中文时必须解析url，否则无法运行）

+ 解析方法一：调用urllib.parse.quote
```
import urllib.request
import urllib.parse
import string

def crawler():
    basis_url = "https://www.baidu.com/s?wd="
    key_word = "中文"
    url = basis_url + key_word  #通过拼接来确定搜索内容
    encode_url = urllib.parse.quote(key_word, safe=string.printable)
    #key_word中出现了中文，通过urllib.parse.quote的方法来解析成python的可识别ASCII字符，其中 safe=string.printable是必须要求填写的

    response = urllib.request.urlopen(encode_url)
    html = response.read().decode("utf-8")
    print(html)

crawler()
```
+ 解析方法二：调用urllib.parse.urlencode()，支持多个参数解析,参数用字典封装起来
    + 通过该方法会直接将字典格式转化成转化为字符串：'wd':'穷哈'  -> 调用方法后：wd = %E7%A9%B7%E5%93%88
    
```
import urllib.request
import urllib.parse
def crawler():
    basis_url = "http://www.baidu.com/s?"
    params = {"wd": "中文","keyword": "你好"}
    encode_url = urllib.parse.urlencode(params)
    print(encode_url)
    url = basis_url + encode_url
    print(url)

crawler()
```
+ data参数的传入
    + 在请求某些网页时需要携带一些数据，我们就需要使用到 data
    + 我们编写时将data编写为一个字典类型，使用时需要被转码成字节流，这就需要需要使用 urllib.parse.urlencode() 将字典转化为字符串，再使用 bytes() 转为字节流，最后使用 urlopen() 发起请求，请求是模拟用 POST 方式提交表单数据
```
import urllib.parse
import urllib.request
def crawler():
    url = "https://cn.bing.com/ttranslatev3?sVertical=1&&IG=2B73CBCDC8F54EAFABF49389E29DC19A&IID=translator.5028.2"
    form_data = {
    "fromLang": "auto-detect",
    "text": "爬虫",
    "to": "en"
    }
    data = bytes(urllib.parse.urlencode(form_data), encoding='utf8')
    response = urllib.request.urlopen(url, data=data)
    print(response.read().decode('utf-8'))

crawler()
```
#### 代理IP的引入

+ 系统的urlopen并没有添加代理的功能所以需要我们自定义这个功能，构建处理器hander和opener
    + 原始的urlopen()方法已经够强大了，但是这并不能满足我们构建一个更加像浏览器的爬虫，所以这时候需要我们自己去构造我们的处理器（handler），然后通过OpenerDirector（opener）去使用处理器，urlopen就是一个Python为我们构造好的opener。
    + Handler 能处理请求（HTTP、HTTPS、FTP等）中的各种事情，它是通过 urllib.request.BaseHandler 这个类来实 现的。urllib.request.BaseHandler是所有的 Handler 的基类，其提供了最基本的Handler的方法
    + 常见的Handler类：
        + ProxyHandler ：为请求设置代理
        + HTTPCookieProcessor ：处理 HTTP 请求中的 Cookies
        + HTTPPasswordMgr ：用于管理密码，它维护了用户名密码的表。
        + HTTPBasicAuthHandler ：用于登录认证，一般和 HTTPPasswordMgr 结合使用。

`创建hander`
```
    import urlib.request

    def myOpener():
        url = "http://www.baidu.com"

        handler = urllib.request.HTTPHandler() #创建自己的hander
          
        opener=urllib.request.build_opener(handler)  #创建自己的oppener
    
        response = opener.open(url) #用自己创建的opener调用open方法请求数据
        data = response.read().decode("utf-8")
        print(data)

    myOpener
```
+ 代理IP的使用（普通）
```
    import urllib.request
    def spider():
        url = "http://www.httpbin.org/ip"
        #proxy为代理IP
        proxy = {   
        "http": "110.243.2.58:9999",
        "http": "117.69.150.100:9999"
        }
        #创建代理IP的hander
        proxy_handler = urllib.request.ProxyHandler(proxy)
        #创建代理IP的opener
        opener = urllib.request.build_opener(proxy_handler)
        #用代理ip去发送请求
        response = opener.open(url)
        data = response.read().decode("utf-8")
        print(data)
        
    spider()

```
+ 代理IP的使用（购买）
```
import urllib.request
def spider():
    #1.添加用户名和密码
    use_name = "name"
    pwd = "123456"
    proxy_money = "代理ip地址"
    #2.创建密码管理器,添加用户名和密码
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    #url 资源定位符
    password_manager.add_password(None,proxy_money,use_name,pwd)
    #3.创建可以验证代理ip的处理器
    handle_auth_proxy = urllib.request.ProxyBasicAuthHandler(password_manager)
    #4.根据处理器创建opener
    opener_auth = urllib.request.build_opener(handle_auth_proxy)
    #5.发送请求
    response = opener_auth.open("http://www.baidu.com")
    print(response.read())


spider()
```
+ 局域网爬取（auth认证）
    + 和购买的IP一样需要输入用户名和密码，创建密码管理器和处理器
```
import urllib.request

def local_area_network():
    #1.添加用户名密码
    user = "admin"
    pwd = "123456"
    local_area_network_url = "http://192...."


    #2.创建密码管理器
    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    pwd_manager.add_password(None,nei_url,user,pwd)

    #创建认证处理器(requests)
    auth_handler = urllib.request.HTTPBasicAuthHandler(pwd_manager)

    opener = urllib.request.build_opener(auth_handler)

    response = opener.open(local_area_network_url)
    print(response)


local_area_network()
```
####cookie介绍
+ 为什么要使用Cookie呢？

    - Cookie，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密）比如说有些网站需要登录后才能访问某个页面，在登录之前，你想抓取某个页面内容是不允许的。那么我们可以利用Urllib库保存我们登录的Cookie，然后再抓取其他页面就达到目的了。
    - 同样urlopen不能满足我们，我们还是需要构建opener
    - 需要使用到的模块：http.cookiejar
```
    import http.cookiejar
    import urllib.request
    def crawler():
        url = "http://tieba.baidu.com/"
        headers = {
        "User-agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50
        (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Cookie": "cookies"
        }
        request = urllib.request.Request(url,headers=headers)
        cookie = http.cookiejar.CookieJar()
        handler = urllib.request.HTTPCookieProcessor(cookie)
        opener = urllib.request.build_opener(handler)
        response = opener.open(requests)
    
    crawler()

```
#### 3.urllib.robotparse
+ 解析robots.txt文件
#### 4.urllib.error
+ 处理urllib.request抛出的异常类型