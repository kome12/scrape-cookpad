import urllib.request

import requests
from bs4 import BeautifulSoup


def getdata(url): 
    r = requests.get(url)
    return r.text 

def scrapepage(pageNumber, index):
  print("starting page number:" + str(pageNumber))
  htmldata = getdata("https://cookpad.com/search/%E3%81%86%E3%81%A9%E3%82%93%20%E7%B0%A1%E5%8D%98?order=date&page=" + pageNumber)
  soup = BeautifulSoup(htmldata, 'html.parser')

  for item in soup.find_all('div', attrs={'class':'recipe-preview'}):
    photo = item.find('img')
    src = photo['src']
    print(str(index) + ": " + src)
    
    req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})

    new_i = '%05d'%(int('00000')+index)
    file_name = new_i + ".jpeg"
    with open('udon/' + file_name, "wb") as f:
        with urllib.request.urlopen(req) as r:
            f.write(r.read())
    index += 1
  return index

def scrapepages():
  index = 1
  for x in range(1000):
    index = scrapepage(str(x + 1), index)

scrapepages()
