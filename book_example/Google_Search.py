#!python3
#Google_Search.py  - Search google results
#Using goolge search url will be like: https://www.google.com/search?q=SEARCH_THERM_HERE
import requests, sys, webbrowser, bs4

searchitem = input('Input search item:')
res = requests.get('http://www.google.com/search?q=' + str(searchitem))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
  webbrowser.open('http://google.com' + linkElems[i].get('href'))