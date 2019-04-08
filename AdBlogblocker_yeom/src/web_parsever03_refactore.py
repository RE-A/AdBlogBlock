#web parsing with beautifulsoup
#from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import js2py

def web_parse(url):     # Function of Open HTML.
    try:
         print('start')
         html = urlopen(url).read().decode('utf-8')
    except HTTPError as e:
        print('fail : ',e.reason)
        html = None
    return html

def get_targeturl(url):      # Function of loading URL.
    host_url = re.findall('https://(.*?)/',url)
    target_url = 'https://'+host_url[0]
    return target_url
    
def Parse():        # Main function of "Parsing Phase"
    inner_html = [] #inner_html url list
    pics, stickers, texts = [],[],[]  # arrays of pic, sticker, text.
  
    target_url = get_targeturl(url)
    html = web_parse(url)
    link = re.findall('<iframe (.*?)>', html)



    for links in link:
        inner_html += re.findall('src="(.*?)"', links)
    print(inner_html) #inner_html is list of string
    links = inner_html[0]#no need to parse hidden html(contain blog music)
    links = target_url+links
    html = web_parse(links)
    pics += re.findall('<img src="(.*?)".*?data-width="(.*?)" data-height="(.*?)".*?class="se-image-resource" />', html)#parse pics number
    stickers += re.findall('<img.*? src="(.*?)".*?class="se-sticker-image" />',html)#parse sticker number
    texts += re.findall('<span.*?>(.*?)</span>',html)#parse text
    #print(pics)
    #print(sticker)
    print(len(pics))
    print(len(stickers))
    print(len(texts))
    for text in texts:
       print(text)

# Lines for Simple debugging.
if __name__ == "__main__":
    url="https://blog.naver.com/kmh03214?Redirect=Log&logNo=221434499140" 


"""     BeautifulSoup is too slow to use parsing program

    for links in link:
       print(links)
       html = web_parse(links)
    soup = BeautifulSoup(html,'html5lib')
    fixed_html = soup.prettify()
    print(fixed_html)   """
