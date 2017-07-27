import requests
from bs4 import BeautifulSoup

#gets headlines
def econ():
        url = 'https://www.economist.com'
        source_code = requests.get(url, allow_redirects=False)
        # just get the code, no headers or anything
        plain_text = source_code.text.encode('ascii', 'replace')
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text, 'html.parser')
        # print(soup.get_text())
        temp=list()
        for link in soup.findAll("a", {"itemprop": "url"}):  # {'class': 's-result-item celwidget '}
            href = link.get("href")

            if "http" in link:
                temp.append(link[link.find("href") + 5:])
            else:
                temp.append(str('https://www.economist.com' + href))
        print(temp)

        return temp[80:]

def nyt():
    url = 'https://www.nytimes.com'
    source_code = requests.get(url, allow_redirects=False)
    # just get the code, no headers or anything
    plain_text = source_code.text.encode('ascii', 'replace')
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text, 'html.parser')

    # print(soup.get_text())
    temp = list()
    for link in soup.findAll("h2", {"class": "story-heading"}):  # {'class': 's-result-item celwidget '}
        href = link.get("a")
        #     title = link.string  # just the text, not the HTML
        # if href==None:
        # continue
        # print(href)
        link=str(link)

        temp.append(link[link.find("href")+5:])
    # #get_single_item_data(href)
    print(temp)
    return temp

def wsj():
    url = 'https://www.wsj.com/'
    source_code = requests.get(url, allow_redirects=False)
    # just get the code, no headers or anything
    plain_text = source_code.text.encode('ascii', 'replace')
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text,'html.parser')

    temp = list()
    #print(soup.get_text())
    for link in soup.findAll("a", {"class": "wsj-headline-link"}):#{'class': 's-result-item celwidget '}
        href = link.get("a")
    #     title = link.string  # just the text, not the HTML
        #if href==None:
            #continue
       # print(href)
        link = str(link)

        temp.append(link[link.find("href") + 5:])
    return temp

def bbc():
    url = 'http://www.bbc.com/news'
    source_code = requests.get(url, allow_redirects=False)
    # just get the code, no headers or anything
    plain_text = source_code.text.encode('ascii', 'replace')
    # BeautifulSoup objects can be sorted through easy
    soup = BeautifulSoup(plain_text, 'html.parser')
    temp = list();
    # print(soup.get_text())
    for link in soup.findAll("a",{'class': 'gs-c-promo-heading nw-o-link-split__anchor gs-o-faux-block-link__overlay-link gel-pica-bold'}):  # {'class': 's-result-item celwidget '}
        link = str(link)

        if "http" in link:
            temp.append(link[link.find("href") + 5:])
        else:
            temp.append(('http://www.bbc.com/news' + link[link.find("href") + 6:]))

    return temp

#gets all new headlines into allnews ################################################333333333333333
allNews=econ()+nyt()+wsj()+bbc()
allNews=[x.lower() for x in allNews]
for line in allNews:
    print(line)
print(len(allNews))



#divides headlines into keywords
import re
keywords=list()
for i in range(len(allNews)):
    keywords += re.split(r'[/-]+| ', allNews[i])

#gets the keywords from the news
import collections
from collections import Counter
counter = collections.Counter(keywords)
for e in ['split__text">the','32','12,''vh@xs','inline"><span','span><h3','svg><','mr','viewbox="0','blogs.wsj.com','top','16','span><','aria','hidden="true"','special','report', 'story','indicator','politics','opinion','The','all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']:
    counter.pop(e,"yes")

#orders the words
orderedwords=counter.most_common()

#removes the 48 useless
for i in range(48):
    orderedwords.pop( 0 )

print(orderedwords)



#search for news headline

