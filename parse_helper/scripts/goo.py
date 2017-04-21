import os.path
import click
import input_helper as ih
import parse_helper as ph
from pprint import pprint


def lazy_filename(text):
    """
    - http://stackoverflow.com/a/7406369
    """
    return "".join([
        c
        for c in text
        if c.isalpha() or c.isdigit() or c in (' ', '-', '_', '+', '.')
    ]).rstrip().replace(' ', '-')


@click.command()
@click.argument('query', nargs=1, default='')
def main(query):
    """Pass a search query to google"""
    query = query or ih.user_input('google query')
    if not query:
        return

    session = ph.new_requests_session()
    selected = ih.make_selections(
        ph.google_serp(query, session=session),
        wrap=False,
        item_format='{title} .::. {link}',
    )
    for item in selected:
        remote_basename = os.path.basename(item['link'])
        ext = remote_basename.split('.')[-1]
        localfile = ''
        if ext != remote_basename:
            localfile = lazy_filename(item['title']) + '.' + ext
        else:
            localfile = lazy_filename(
                item['link'].split('://')[-1].strip('/').replace('/', '--')
            ) + '.html'
        ph.download_file(item['link'], localfile, session=session)


if __name__ == '__main__':
    main()
