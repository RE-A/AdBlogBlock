# -*- coding: utf-8 -*-
from CrawlFunction import *

# 검색어는 여기다가 입력
searchWord = "강남 미용실" 
#  몇 개의 글을 검색할 것인가? 10 단위로 가능.
MAX_NUMBER_TO_SEARCH = 10 

################################################################

maxnum = int(MAX_NUMBER_TO_SEARCH/10)
url = setURL(searchWord)
f = open("TestModule/result.txt", "w", encoding='utf8')

for i in range(1,maxnum):
    html = getSiteHtml(url)
    results = html.findAll('li',{'class':'sh_blog_top'})
    for result in results:
        title = str(result.dl.dt.a['title'])+'\n'
        f.write(title)

f.close()