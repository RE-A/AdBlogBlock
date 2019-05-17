import CrawlFunction
import crawl
from Parsing import *

# 검색어는 여기다가 입력
searchWord = "신림 미용실" 
#  몇 개의 글을 검색할 것인가? 10 단위로 가능.
#  10~1000개까지 가능. 네이버 검색결과가 1000건까지만 보여주기 때문
MAX_NUMBER_TO_SEARCH = 10
##########################################################################

crawl.CrawlURL(searchWord,MAX_NUMBER_TO_SEARCH)
f = open('TestModule/CrawlResult.txt','r',encoding='utf8')
lines= f.readlines()
for line in lines:
    Parse(line)
f.close()

