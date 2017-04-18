from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#Listing for internal links of current page
def getInternalLinks(bsObj, includeUrl):
	internalLinks = []
	#find URLs that start with "/"
	for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks

#Listing for external links of current page
def getExternalLinks(bsObj, excludeUrl):
	externalLinks = []
	#find urls that include "http" or "www"  and exclude current page url
	for link in bsObj.findAll("a", href=re.compile("^(http|https|www)((?!" + excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	addressParts = address.replace("http://","").split("/")
	return addressParts

def getRandomExternalLink(startingPage):
	html = urlopen(startingPage)
	bsObj = BeautifulSoup(html, "html.parser")
	externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
	if len(externalLinks) == 0:
		internalLinks = getInternalLinks(startingPage)
		print("external link is zero, instead internal links are " + internalLinks)
		return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink(startingSite)
	print("Random external link is: "+externalLink)
	followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")
