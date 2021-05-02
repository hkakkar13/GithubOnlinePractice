from bs4 import BeautifulSoup
import urllib.request 

android_url = urllib.request.urlopen("https://en.wikipedia.org/wiki/Android_version_history")

android_urlResponse = android_url.read()

##print(android_urlResponse)

soup = BeautifulSoup(android_urlResponse,'html.parser')
soup.name

