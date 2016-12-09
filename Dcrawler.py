# -*- coding: utf8 -*-

import re, urllib2
import json
from bs4 import BeautifulSoup

jsonData = list()
result = list()
#https://www.dcard.tw/api/post/all/147060 ====== dcard article content api resObj['version'][0]['content']
'''
multi
'''
for i in range(30):
    url = "https://www.dcard.tw/_api/forums/sex/"
    url+=str(i+1)
    url+="/"
    print url
    html = urllib2.urlopen(url).read()
    if html != '[]':
        data  = json.loads(html)
        for n in data:
            if re.findall( u"圖", n['version'][0]['title']):
                if n['member']['gender']==u"F":
                    jsonData.append(n)
for i in jsonData:
    # print "https://www.dcard.tw/f/sex/p/"+str(i['id'])
    print "<a href='https://www.dcard.tw/f/sex/p/"+ str(i['id']) +"'>Link</a>"
    result.append("<a href='https://www.dcard.tw/f/sex/p/"+ str(i['id']) +"'>Link</a>")

'''
single
'''
# url = "https://www.dcard.tw/api/forum/sex/"
# url+=str(3)+"/"
# html = urllib2.urlopen(url).read()
# data  = json.loads(html)
# #data = json.dumps(data, ensure_ascii=False)

# for n in data:
#     if re.findall( u"圖", n['version'][0]['title']):
#         if n['member']['gender']==u"F":
#             jsonData.append(n)

# for i in jsonData:
#     print "https://www.dcard.tw/f/sex/p/"+str(i['id'])


'''
output
'''
data = json.dumps(result, ensure_ascii=False, sort_keys=False).encode('utf-8')

with open("Dcrawler.html", "w") as f:
	f.write(data)
