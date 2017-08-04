import requests
from bs4 import BeautifulSoup

import re
import collections
from collections import Counter

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
def allNews():
    allNews=econ()+nyt()+wsj()+bbc()
    allNews=[x.lower() for x in allNews]
    print(len(allNews))
    return allNews

#divides headlines into words
def words():
    keywords=list()
    headlines=allNews()
    for i in range(len(headlines)):
        keywords += re.split(r'[/-]+| ', headlines[i])
    return keywords

#gets the keywords from the words and orders them
def keywords():
    wordlist=words()
    counter = collections.Counter(wordlist)
    for e in ['make','science','media','07','split__text">the','32','12,''vh@xs','inline"><span','span><h3','svg><','mr','viewbox="0','blogs.wsj.com','top','16','span><','aria','hidden="true"','special','report', 'story','indicator','politics','opinion','The','all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once']:
        counter.pop(e,"yes")
    orderedwords=counter.most_common()
    # removes the 48 useless
    for i in range(48):
        orderedwords.pop(0)
    return orderedwords

#search for news headline
def keywordSearch():
    keysearch = input('Enter keyword:')
    keysearch=keysearch.lower()
    print('\n\n\n\n\n\n')
    headlines=allNews()
    for line in headlines:
        if(keysearch in line):
            print(line)


#track news headlines daily

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=10)
def timed_job():
    print(allNews())
    print(keywords())
    print('This job is run every 10 seconds.')
    keywordSearch()



@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
def scheduled_job():
    print('This job is run every weekday at 10am.')

sched.start()