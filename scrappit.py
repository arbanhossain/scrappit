#libraries
import urllib.request as url
from bs4 import BeautifulSoup as bs

def scrape(subreddit, flairname):
    siteUrl = 'https://reddit.com'
    pageUrl = siteUrl + '/r/' + subreddit
    page = url.urlopen(pageUrl)

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

        if flairname is not '':
            if flair.text == flairname:
                if flair is not None: print(flair.text)
                if title is not None: print(title.text)
                if link is not None: print(siteUrl+link['href'])
                print('\n')
        
        else:
            if flair is not None: print(flair.text)
            if title is not None: print(title.text)
            if link is not None: print(siteUrl+link['href'])
            print('\n')



subreddit = input('subreddit: ')
flairname = input('flair: ')

scrape(subreddit, flairname)
