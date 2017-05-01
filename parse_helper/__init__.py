import requests
import time
import logging
import os.path
from bs4 import BeautifulSoup, FeatureNotFound


requests.packages.urllib3.disable_warnings()
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36'
_JSON_TYPES = (
    'application/javascript'
    'application/json'
    'application/x-javascript'
    'text/javascript'
    'text/x-javascript'
    'text/x-json'
)

LOGFILE = os.path.abspath('log--parse-helper.log')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(LOGFILE, mode='a')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(funcName)s: %(message)s'
))
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
logger.addHandler(file_handler)
logger.addHandler(console_handler)


def new_requests_session():
    """Return a new requests Session object"""
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    logger.debug('New session created')
    return session


def fetch_html(url, session=None):
    """Fetch url and return the page's html (or None)

    - url: a string
    - session: a session object
    """
    session = session or new_requests_session()
    logger.info('Fetching HTML from {}'.format(url))
    try:
        response = session.head(url)
    except requests.exceptions.ConnectionError:
        logger.error('Could not access {}'.format(repr(url)))
    else:
        if 'text/html' in response.headers['content-type']:
            response = session.get(url, verify=False)
            return response.content
        else:
            logger.error('{} is not HTML content... {}'.format(
                repr(url),
                response.headers['content-type']
            ))


def fetch_json(url, session=None):
    """Fetch url and return a dict for the JSON data (or None)

    - url: a string
    - session: a session object
    """
    session = session or new_requests_session()
    logger.info('Fetching JSON from {}'.format(url))
    try:
        response = session.head(url)
    except requests.exceptions.ConnectionError:
        logger.error('Could not access {}'.format(repr(url)))
    else:
        if response.headers['content-type'] in _JSON_TYPES:
            response = session.get(url, verify=False)
            return response.json()
        else:
            logger.error('{} is not JSON content... {}'.format(
                repr(url),
                response.headers['content-type']
            ))


def get_soup(url_or_file, session=None):
    """Fetch url (or open a file) and return a BeautifulSoup object (or None)

    - url_or_file: a string
    - session: a session object
    """
    html = ''
    if os.path.isfile(url_or_file):
        with open(url_or_file, 'r') as fp:
            html = fp.read()
    else:
        html = fetch_html(url_or_file, session)

    if html:
        try:
            return BeautifulSoup(html, 'lxml')
        except FeatureNotFound:
            return BeautifulSoup(html)


def download_file(url, localfile='', session=None):
    """Download file using `requests` with stream enabled

    - url: a string
    - localfile: a string
    - session: a session object

    See: http://stackoverflow.com/questions/16694907/
    """
    session = session or new_requests_session()
    localfile = localfile or os.path.basename(url)

    for sleeptime in [5, 10, 30, 60]:
        try:
            logger.info('Saving {} to {}'.format(repr(url), repr(localfile)))
            r = session.get(url, stream=True)
            with open(localfile, 'wb') as fp:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        fp.write(chunk)
                        fp.flush()

            break
        except Exception as e:
            logger.error('{}... sleeping for {} seconds'.format(repr(e), sleeptime))
            session.close()
            time.sleep(sleeptime)
            session = new_requests_session()


from .parser import *
