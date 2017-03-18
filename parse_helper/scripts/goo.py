import click
import input_helper as ih
import parse_helper as ph
from pprint import pprint


@click.command()
@click.argument('query', nargs=1, default='')
def main(query):
    """Pass a search query to google"""
    query = query or ih.user_input('google query')
    if not query:
        return

    selected = ih.make_selections(
        ph.google_serp(query),
        wrap=False,
        item_format='{title} .::. {link}',
    )
    if selected:
        ph.logger.info('Selected {}'.format(' '.join([x['link'] for x in selected])))
        with open(ph.LOGFILE, 'a') as fp:
            pprint(selected, fp)


if __name__ == '__main__':
    main()
