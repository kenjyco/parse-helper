import click
import input_helper as ih
import parse_helper as ph
from pprint import pprint


@click.command()
@click.argument('query', nargs=1, default='')
def main(query):
    """Pass a search query to duckduckgo api"""
    query = query or ih.user_input('duckduckgo query')
    if not query:
        return

    selected = ih.make_selections(
        ph.duckduckgo_api(query),
        wrap=True,
        item_format='{text}',
    )
    if selected:
        ph.logger.info('Selected {}'.format(' '.join([x['link'] for x in selected])))
        with open(ph.LOGFILE, 'a') as fp:
            pprint(selected, fp)


if __name__ == '__main__':
    main()
