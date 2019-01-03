import os
import urllib.request as url
import difflib
from bs4 import BeautifulSoup as bs

SITEURL = 'https://reddit.com'


def matchWords(keywords, title):
    score = 0
    if title is None:
        return 0
    titleWords = title.text.split(' ')
    for x in keywords:
        if(len(difflib.get_close_matches(x, titleWords)) > 0):
            score = score + 1
    return score


def printEach(flair, title, link):
    if flair is not None:
        print(flair.text)
    if title is not None:
        print(title.text)
    if link is not None:
        print(SITEURL+link['href'])
    print('\n')


def printStuff(flairname, flair, keywords, title, link):
    if flairname is not '':
        if keywords == ['']:
            if flair is not None and flair.text == flairname:
                printEach(flair, title, link)
        else:
            matchScore = matchWords(keywords, title)
            if matchScore > 0 and flair is not None and flair.text == flairname:
                printEach(flair, title, link)

    else:
        if keywords == ['']:
            printEach(flair, title, link)
        else:
            matchScore = matchWords(keywords, title)
            if matchScore > 0:
                printEach(flair, title, link)


def scrape(subreddit, flairname, keywords):
    if subreddit is '':
        return False
    pageUrl = SITEURL + '/r/' + subreddit
    request = url.Request(pageUrl)
    userAgent = os.getenv('USERAGENT', default='Mozilla/5.0')
    request.add_header('User-Agent', userAgent)

    page = url.urlopen(request).read()

    divClass = ['scrollerItem']
    titleClass = ['imors3-0', 'iuScIP']
    linkClass = ['SQnoC3ObvgnGjWt90zD9Z']
    flairClass = ['nfc34t-2', 'jrvAPZ']

    soup = bs(page, 'html.parser')
    divs = soup.find_all('div', attrs={'class': ' '.join(divClass)})

    length = len(divs)

    for div in divs:
        flair = div.find('span', attrs={'class': ' '.join(flairClass)})
        title = div.find('h2', attrs={'class': ' '.join(titleClass)})
        link = div.find('a', attrs={'class': ' '.join(linkClass)})

        printStuff(flairname, flair, keywords, title, link)


if __name__ == '__main__':
    subreddit = input('subreddit: ')
    flairname = input('flair: ')
    keywords = input('enter space separated keywords: ').split(' ')

    scrape(subreddit, flairname, keywords)
