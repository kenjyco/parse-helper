import os.path
import click
import input_helper as ih
import parse_helper as ph
import fs_helper as fh
from pprint import pprint


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
            localfile = fh.lazy_filename(
                ph.get_domain(item['link']) + '--' + item['title'],
                ext=ext
            )
        else:
            localfile = fh.lazy_filename(
                item['link'],
                ext='html'
            )
        ph.download_file(item['link'], localfile, session=session)


if __name__ == '__main__':
    main()
