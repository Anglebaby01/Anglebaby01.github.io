# -*- coding: utf-8 -*-
import requests
from lxml import etree
import  io
import sys
def crawler():

    url = "https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0xfed2c8ed0035172d&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=78000241_9_hao_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=3&rsv_sug1=3&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=1307&rsv_sug4=2576"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'Cookie':'BAIDUID=A73587ED4F3222B80C4FE16CB6B65DD7:FG=1; BIDUPSID=A73587ED4F3222B80C4FE16CB6B65DD7; PSTM=1587136751; BD_UPN=12314753; yjs_js_security_passport=0e6646cc08e32d531de1788125bb23f41137a2c9_1588410443_js; BDUSS=FBOUNaOUhFMDdwQjhyLTBIS3FVZElEbm85c2l3cnYwajNSVUVOZTFVVEJFTlZlRVFBQUFBJCQAAAAAAAAAAAEAAADiLOpIs8K80eL5tcTE0MXz09EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMGDrV7Bg61eQU; BDPASSGATE=IlPT2AEptyoA_yiU4VKP3kIN8efjSri4D4eGSyRpQFStfCaWmhH3BrUzWz0HSieXBDP6wZTXdMsDxXTqXlVXa_EqnBsZolpOaSaXzKGoucHtVM69-t5yILXoHUE2sA8PbRhL-3MEF2ZELkwvcgjchQZrchW8z3Ibhx0shE76cfbW16nyZ-r-m6qF1VlHU-usNPWx9486mCgdPpyBUuL2LTTtmU19QJ1R7Aq7is5qOQD7vSEzD2KmL3YhGG85Jppg0huP3OyLxRWlFSoZwp-tKCkYjkiY6qjxSUIS2Kbpz1NeO1K; H_WISE_SIDS=144089_143435_142019_144427_145945_140632_146113_145870_144420_144134_145271_146538_146308_145303_144961_131247_144681_141261_144250_141941_127969_146037_146549_140594_142421_145876_131423_100805_145909_146001_145598_107315_146135_139909_146395_144966_142427_145608_140367_143665_144018_146054_145397_143860_145073_139913_110085; SE_LAUNCH=5%3A26473974; MSA_WH=774_922; MSA_PBT=146; MSA_PHY_WH=1548_1844; MSA_ZOOM=1056; FC_MODEL=0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_1588438456%7C1%230_0_0_0_0_0_1588438456%7C1%230__0_0_0_0_351_1588438456; wpr=0; BDRCVFR[Y1-7gJ950Fn]=OjjlczwSj8nXy4Grjf8mvqV; BD_HOME=1; H_PS_PSSID=; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_645EC=4b056V7e%2Fk2YRqGMTC3b46ni%2FRA6WwQji2etuSJlHsv%2FgYT9LZQGZVIvIqX7WOFcpwkmg5rQr5E; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; COOKIE_SESSION=573255_0_1_0_2_1_1_0_0_1_2_0_0_0_3_0_1587895012_0_1588468264%7C2%230_0_1588468264%7C1; BDSVRTM=0'
    }
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
    #解决UnicodeEncodeError: 'gbk' codec can't encode character '\ue780' in position 439546: illegal multibyte sequence
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    ip_result = html.xpath('//*[@id="1"]/div/div/div/table/tr/td/span/text()')[0]
    print(ip_result[:5],ip_result[6:len(ip_result)-1])

    #print(etree.tostring(html, encoding='utf-8').decode('utf-8'))


    #print(response.content.decode('utf-8'))
crawler()