import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# ahcnor tag은 <a></a>로 된 태그
#그러므로 아래 tags는 뭇너 안에 있는 모든 태그를 모아서 돌려줌.
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
