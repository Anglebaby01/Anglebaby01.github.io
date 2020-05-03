XPath，全称XML Path Language，即XML路径语言，它是一门在XML文档中查找信息的语言。其功能强大，提供了非常简洁明了的路径选择表达式。XPath筛选后的结果返回为列表。

常用规则
|表达式|描述|
|---|---|
|nodename|	此节点的所有子节点|
|/	|从当前节点选取直接子节点|
|//	|从当前节点选取子孙节点|
|.	|选取当前节点}
|..	|选取当前节点的父节点|
|@	|选取属性|
基本使用方法
```
from lxml import etree

### 把html文件保存到本地，命名test
text = """
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
"""

# 基本使用
html = etree.parse('./test.html', etree.HTMLParser())
# 所有节点
result = html.xpath('//*')
# 子节点
result = html.xpath('//li/a')
# 父节点
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# 属性匹配
result = html.xpath('//li[@class="item-0"]')
# 文本获取
result = html.xpath('//li[@class="item-0"]/a/text()')
# 属性获取
result = html.xpath('//li/a/@href)
# 属性多值匹配
result = html.xpath('//li[contains(@class, "li")]/a/text()')
# 多属性匹配
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# 按序选择
result = html.xpath('//li[last()]/a/text()')
# 节点轴选择
result = html.xpath('//li[1]/ancestor::*')
# 拼接同级标签内容
total = html.xpath('concat(//span[@class="total"]/span/text(),//span[@class="unit"]/span/text())')
```