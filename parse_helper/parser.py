__all__ = [
    'soup_explore', 'duckduckgo_api',
]


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
