###reuquests库
+ 衍生与urllib库，比urllib库更加强大和实用
+ 属于第三方库，需要下载安装
# requests库爬虫标准
```
import requests

url = 'http://www.baidu.com'
headers = {
    'User-Agent':'Mozilla/5.0'
}
try:
    response = requests.get(url, headers = headers)
    response.raise_for_status()
    response.encoding = r.apparent_encoding
    return response.text
except:
    print('爬取失败')
```
### 实例引入
```
import requests

response = requests.get('https://www.baidu.com/')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
```
### 各种请求方式
```
import requests

requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')
```
### 带参数的get请求
```
import requests

data = {
    'name':'gemey',
    'age':22
}
response = requests.get('http://httpbin.org/get', params=data)
print(response.text)
```
### 转换成json格式
```
import requests
import json

response = requests.get('https://httpbin.org/get')
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
```
### 获取二进制数据
```
import requests

response = requests.get('http://github.com/favicon.ico')
with open('favicon.ico','wb') as f:
    f.write(response.content)
    f.close()
```
### 添加headers
```
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
response = requests.get('https://www.zhihu.com/explore', headers=headers)
print(response.text)
```
#### 高级用法
### 文件上传
```
import requests

files = {'file':open('favicon.ico', 'rb')}
response = requests.post('http://httpbin.org/post', files=files)
print(response.text)
```
### 获取cookies
```
import requests

response = requests.get('http://www.baidu.com')
print(response.cookies)
for key, value in response.cookies.items():
    print(key + '=' + value)
```
### 会话维持
```
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)
```


### 异常处理
```
import requests

try:
    response = requests.get('http://httpbin.org/get', timeout=0.1)
    print(response.status_code)
except Exception as e:
    print(e)
```
### 图片下载保存路径和命名方法
```
import requests
import os


url = 'https://img10.360buyimg.com/n5/s75x75_jfs/t1/42272/20/10323/135815/5d3d6adfE63e2cb03/7c966e6a71f02044.jpg'
headers = {
    'User-Agent':'Mozilla/5.0'
}
root = 'D://images//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        with open(path, 'wb') as f:
            f.write(response.content)
            f.close()
            print('文件下载完成')
    else:
        print('文件已存在')
except:
    print('爬取失败')
打印出现中文乱码
```
### 以网页编码格式解析
```
response.encoding = response.apparrent_code
```
### 先返回二进制格式，再转码成utf-8
```
response.content.decode('utf-8')
```
    