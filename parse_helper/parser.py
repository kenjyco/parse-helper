__all__ = ['soup_explore', 'duckduckgo_api', 'google_serp', 'youtube_serp']


import re
import parse_helper as ph
from IPython import embed


def soup_explore(url_or_file, session=None):
    """Given a url or file, get a soup object from it and start ipython session

    - url_or_file: a string
    - session: a session object
    """
    soup = ph.get_soup(url_or_file, session)
    if not soup:
        ph.logger.error('No soup found for {}'.format(url_or_file))
    else:
        print('\nExplore the "soup" object\n\n')
        embed()
    return soup


def duckduckgo_api(query, session=None):
    """Return a list of dicts containing results from the query

    - query: a string
    - session: a session object
    """
    query = query.replace(' ', '+')
    url = 'https://api.duckduckgo.com?q={}&format=json'.format(query)
    data = []
    json_data = ph.fetch_json(url, session)
    if not json_data:
        ph.logger.error('No JSON data found for {}'.format(url))
        return data

    data.extend([
        {
            'text': result['Text'],
            'thumbnail': result['Icon']['URL'],
            'link': result['FirstURL'],
        }
        for result in json_data['Results']
    ])

    for result in json_data['RelatedTopics']:
        if 'Topics' in result:
            data.extend([
                {
                    'text': r['Text'],
                    'thumbnail': r['Icon']['URL'],
                    'link': r['FirstURL'],
                    'topic': result['Name'],
                }
                for r in result['Topics']
            ])
        else:
            data.append({
                'text': result['Text'],
                'thumbnail': result['Icon']['URL'],
                'link': result['FirstURL'],
            })

    return data


def google_serp(query, session=None):
    """Return a list of dicts containing results from the query

    - query: a string
    - session: a session object
    """
    query = query.replace(' ', '+')
    url = 'https://www.google.com/search?q=' + query
    data = []
    soup = ph.get_soup(url, session)
    if not soup:
        ph.logger.error('No soup found for {}'.format(url))
        return data

    for h3 in soup.find_all('h3', attrs={'class': 'r'}):
        result_data = {}
        result_data['link'] = h3.a.attrs['href']
        result_data['title'] = h3.a.text
        data.append(result_data)

    return data


def youtube_serp(query, session=None):
    """Return a list of dicts containing results from the query

    - query: a string
    - session: a session object
    """
    query = query.replace(' ', '+')
    url = 'https://www.youtube.com/results?search_query=' + query
    data = []
    soup = ph.get_soup(url, session)
    if not soup:
        ph.logger.error('No soup found for {}'.format(url))
        return data

    section = soup.find(attrs={'class': 'item-section'})
    results = section.find_all(attrs={'class': 'yt-lockup-content'})

    for result in results:
        result_data = {}
        try:
            result_data['link'] = 'https://www.youtube.com' + result.h3.a.attrs['href']
            result_data['title'] = result.h3.a.attrs['title']
        except AttributeError:
            continue
        try:
            result_data['duration'] = _clean_youtube_duration(result.h3.span.text)
        except AttributeError:
            result_data['duration'] = ''
        try:
            result_data['user'] = result.find(attrs={'class': 'yt-lockup-byline'}).a.text
        except AttributeError:
            result_data['user'] = ''
        try:
            metadata = result.find(attrs={'class': 'yt-lockup-meta-info'})
            metadata = [x.text for x in metadata.findChildren()]
        except AttributeError:
            metadata = []
        try:
            result_data['uploaded'] = metadata[0]
            result_data['views'] = metadata[1]
        except IndexError:
            result_data['uploaded'] = ''
            result_data['views'] = ''

        data.append(result_data)

    return data


def _clean_youtube_duration(text):
    rx = re.compile(r' - Duration: ([\S]+)\.')
    match = rx.match(text)
    if match:
        return match.group(1)

    return 'playlist'
