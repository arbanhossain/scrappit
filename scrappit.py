import sys
import os
from argparse import ArgumentParser
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
    if keywords == ['']:
        printEach(flair, title, link)
    elif flairname is not '':
        matchScore = matchWords(keywords, title)
        if matchScore > 0 and flair is not None and flair.text == flairname:
            printEach(flair, title, link)
    else:
        matchScore = matchWords(keywords, title)
        if matchScore > 0:
            printEach(flair, title, link)


def scrape(subreddit, flairname, keywords):
    pageUrl = SITEURL + '/r/' + subreddit
    request = url.Request(pageUrl)
    userAgent = os.getenv('USERAGENT', default='Mozilla/5.0')
    request.add_header('User-Agent', userAgent)

    try:
        page = url.urlopen(request).read()
    except Exception as e:
        print(e)
        sys.exit()

    divClass = ['scrollerItem']
    titleClass = ['imors3-0', 'iuScIP']
    linkClass = ['SQnoC3ObvgnGjWt90zD9Z']
    flairClass = ['nfc34t-2', 'jrvAPZ']

    soup = bs(page, 'html.parser')
    divs = soup.find_all('div', attrs={'class': ' '.join(divClass)})

    for div in divs:
        flair = div.find('span', attrs={'class': ' '.join(flairClass)})
        title = div.find('h2', attrs={'class': ' '.join(titleClass)})
        link = div.find('a', attrs={'class': ' '.join(linkClass)})
        printStuff(flairname, flair, keywords, title, link)


if __name__ == '__main__':
    parser = ArgumentParser(
                description='Scrape a subreddit and search for keyword',
            )

    parser.add_argument('subreddit',
                        help='the subreddit to search in')
    parser.add_argument('-f', '--flair', default='',
                        help='name of the flair (optional)')
    parser.add_argument('-k', '--keywords', nargs='*',
                        help='keywords to search for')

    args = parser.parse_args()

    scrape(args.subreddit, args.flair, args.keywords)
