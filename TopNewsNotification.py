import requests
from bs4 import BeautifulSoup


def econ():
        url = 'https://www.economist.com'
        source_code = requests.get(url, allow_redirects=False)
        # just get the code, no headers or anything
        plain_text = source_code.text.encode('ascii', 'replace')
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text, 'html.parser')
        # print(soup.get_text())
        for link in soup.findAll("a", {"itemprop": "url"}):  # {'class': 's-result-item celwidget '}
            href = link.get("href")
            print('https://www.economist.com'+href)

        return soup.findAll("a", {"itemprop": "url"})

def nyt():
    url = 'https://www.nytimes.com'
    source_code = requests.get(url, allow_redirects=False)
    # just get the code, no headers or anything
    plain_text = source_code.text.encode('ascii', 'replace')
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text, 'html.parser')

    # print(soup.get_text())
    for link in soup.findAll("h2", {"class": "story-heading"}):  # {'class': 's-result-item celwidget '}
        href = link.get("a")
        #     title = link.string  # just the text, not the HTML
        # if href==None:
        # continue
        # print(href)
        link=str(link)
        print(link[link.find("href")+5:])
    # #get_single_item_data(href)
    return soup.findAll("h2", {"class": "story-heading"})

def wsj():
    url = 'https://www.wsj.com/'
    source_code = requests.get(url, allow_redirects=False)
    # just get the code, no headers or anything
    plain_text = source_code.text.encode('ascii', 'replace')
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text,'html.parser')


    #print(soup.get_text())
    for link in soup.findAll("a", {"class": "wsj-headline-link"}):#{'class': 's-result-item celwidget '}
        href = link.get("a")
    #     title = link.string  # just the text, not the HTML
        #if href==None:
            #continue
       # print(href)
        link = str(link)
        print(link[link.find("href") + 5:])
    return soup.findAll("a", {"class": "wsj-headline-link"})

def bbc():
    url = 'http://www.bbc.com/news'
    source_code = requests.get(url, allow_redirects=False)
    # just get the code, no headers or anything
    plain_text = source_code.text.encode('ascii', 'replace')
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text, 'html.parser')

    # print(soup.get_text())
    for link in soup.findAll("a",{'class': 'gs-c-promo-heading nw-o-link-split__anchor gs-o-faux-block-link__overlay-link gel-pica-bold'}):  # {'class': 's-result-item celwidget '}
        link = str(link)
        if "http" in link:
            print(link[link.find("href") + 5:])
        else:
            print('http://www.bbc.com/news' + link[link.find("href") + 6:])

    return soup.findAll("a",{'class': 'gs-c-promo-heading nw-o-link-split__anchor gs-o-faux-block-link__overlay-link gel-pica-bold'});

#adding new
allNewsRaw = econ()+nyt()+wsj()+bbc()
allNews=str(allNewsRaw)

#print(allNe ws)
from nltk.corpus import words
word_list = words.words()

import re, collections
w=["Syria","Trump","Mccain"]
pattern = re.compile("|".join(w), flags = re.IGNORECASE)
print(collections.Counter(pattern.findall(allNews)))

