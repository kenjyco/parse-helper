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
@click.option(
    '--page', 'page', default=1, type=click.INT,
    help='page number of results'
)
@click.option(
    '--since', 'since', default='', type=click.Choice([
        '', 'year', 'month', 'week', 'day'
    ]),
    help='limit results by time'
)
@click.option(
    '--site', 'site', default='',
    help='limit results by site/domain'
)
@click.option(
    '--filetype', 'filetype', default='', type=click.Choice([
        '', 'pdf', 'xls', 'ppt', 'doc', 'rtf'
    ]),
    help='limit results by filetype'
)
def main(query, **kwargs):
    """Pass a search query to google"""
    query = query or ih.user_input('google query')
    if not query:
        return

    session = ph.new_requests_session()
    selected = ih.make_selections(
        ph.google_serp(query, session=session, **kwargs),
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
