#t시작 URL에서 부터 (랜덤하게)타고 타고 들어가서 href 항목 없을 때까지 url lising
#링크에서 링크로 무작위 이동
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle) #새 페이지에서 항목(URL) 리스트를 가져오기
