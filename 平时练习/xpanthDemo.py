from lxml import etree
html = etree.parse("hello.html")
result = html.xpath("//li//text()")
#print(result)
# for i in result:
#     print(etree.tostring(i).decode('utf-8'))
# result2= html.xpath("//li/@class")
# result = html.xpath("//li/a[@href='link1.html']/text()")
# result2 = html.xpath("//li/a/span/text()")
# result2=html.xpath("//li/@class")
result2 = html.xpath("//li//a[@href='link1.html']/text()")
print(result2)

#print(result[0].text)