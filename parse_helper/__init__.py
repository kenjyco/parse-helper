import requests
from bs4 import BeautifulSoup, FeatureNotFound


requests.packages.urllib3.disable_warnings()
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36'


def new_requests_session():
    """Return a new requests Session object"""
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    return session


def fetch_html(url, session=None):
    """Fetch url and return the page's html (or None)"""
    session = session or new_requests_session()
    try:
        response = session.head(url)
    except requests.exceptions.ConnectionError:
        print('Could not access {}'.format(repr(url)))
    else:
        if 'text/html' in response.headers['content-type']:
            response = session.get(url, verify=False)
            return response.content
        else:
            print('Not html content')


def get_soup(url, session=None):
    """Fetch url and return a BeautifulSoup object (or None)"""
    html = fetch_html(url, session)
    if html:
        try:
            return BeautifulSoup(html, 'lxml')
        except FeatureNotFound:
            return BeautifulSoup(html)


from .parser import *
