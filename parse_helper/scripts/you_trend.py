import click
import input_helper as ih
import parse_helper as ph
from pprint import pprint


@click.command()
def main():
    """Select from current trending on youtube"""
    selected = ih.make_selections(
        ph.youtube_trending(),
        wrap=False,
        item_format='{duration} .::. {title} .::. {user} .::. {uploaded}',
    )
    if selected:
        ph.logger.info('Selected {}'.format(' '.join([x['link'] for x in selected])))
        with open(ph.LOGFILE, 'a') as fp:
            pprint(selected, fp)


if __name__ == '__main__':
    main()
