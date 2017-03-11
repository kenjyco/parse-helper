import requests
import time
import logging
from bs4 import BeautifulSoup, FeatureNotFound


requests.packages.urllib3.disable_warnings()
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36'

LOGFILE = 'log--parse-helper.log'
logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(funcName)s: %(message)s',
        level=logging.DEBUG,
        filename=LOGFILE,
        filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


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


def download_image(url, localfile, session=None):
    """Download image using `requests` with stream enabled

    See: http://stackoverflow.com/questions/16694907/
    """
    session = session or new_requests_session()

    for sleeptime in [5, 10, 30, 60]:
        try:
            logging.info('Saving {} to {}'.format(repr(url), repr(localfile)))
            r = session.get(url, stream=True)
            with open(localfile, 'wb') as fp:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        fp.write(chunk)
                        fp.flush()

            break
        except Exception as e:
            logging.error('{}... sleeping for {} seconds'.format(repr(e), sleeptime))
            session.close()
            time.sleep(sleeptime)
            session = new_requests_session()


from .parser import *
