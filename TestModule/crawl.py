# -*- coding: utf-8 -*-
from CrawlFunction import *

# 검색어는 여기다가 입력
searchWord = "강남 미용실" 
#  몇 개의 글을 검색할 것인가? 10 단위로 가능.
MAX_NUMBER_TO_SEARCH = 20 

################################################################

maxnum = int(MAX_NUMBER_TO_SEARCH/10)
url = setURL(searchWord)
f = open("TestModule/result.txt", "w", encoding='utf8')

for i in range(1,maxnum+1):
    html = getSiteHtml(url)
    results = html.findAll('li',{'class':'sh_blog_top'})

    for result in results:
        title = result.find('a',{'class':'sh_blog_title _sp_each_url _sp_each_title'})
        title = title['title']+'\n'
        f.write(title)

    url = "https://search.naver.com/search.naver"+html.find('a',{'class':'next'})['href']
f.close()