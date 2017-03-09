__all__ = ['google_serp', 'youtube_serp']


import re
import parse_helper as ph


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
        return []

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
        return []

    section = soup.find(attrs={'class': 'item-section'})
    results = section.find_all(attrs={'class': 'yt-lockup-content'})

    for result in results:
        result_data = {}
        result_data['link'] = 'https://www.youtube.com' + result.h3.a.attrs['href']
        result_data['title'] = result.h3.a.attrs['title']
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
