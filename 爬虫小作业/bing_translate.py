import requests
import json
def bingTranslate():
    text = input('请输入你要翻译的语句（中 -> 英）：')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    }
    url = 'https://cn.bing.com/ttranslatev3?isVertical=1&&IG=07B681A73A8C4F059F058F12AC6279F5&IID=translator.5027.2'
    data = {
        'fromLang': 'auto-detect',
        'text': text,
        'to': 'en'
    }
    response = requests.post(url=url,data=data,headers=headers)
    response = json.loads(response.text)
   # print(response)
    print('翻译结果为：',end=' ')
    print(response[0]['translations'][0]['text'])
bingTranslate()