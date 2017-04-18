# 해당 위키 백과에서 다른 항목(인물) 링크들 리스팅

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")
for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki)((?!:).)*$")):
#    print(link)
    if "href" in link.attrs:
        print(link.attrs['href'])
