#!python3
#Google_Search.py  - Search google results
#Using goolge search url will be like: https://www.google.com/search?q=SEARCH_THERM_HERE
#Need to update soup.select elem for google web html.
import requests, sys, webbrowser, bs4

proxy = {
  'http':'127.0.0.1:10809',
  'https':'127.0.0.1:10809',
}
searchitem = input('Input search item:')
res = requests.get('http://www.google.com/search?q=' + ''.join(str(searchitem)), proxies = proxy)
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,'html.parser')

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
try:
  for i in range(numOpen):
    webbrowser.open('http://www.google.com' + linkElems[i].get('href'))
except requests.exceptions.ConnectionError:
  print('Failed to connect to google.')
