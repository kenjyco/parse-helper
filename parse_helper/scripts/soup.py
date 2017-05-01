import click
import input_helper as ih
import parse_helper as ph


@click.command()
@click.argument('url_or_file', nargs=1, default='')
def main(url_or_file):
    """Create a soup object from a url or file and explore with ipython"""
    url_or_file = url_or_file or ih.user_input('url')
    ph.soup_explore(url_or_file)


if __name__ == '__main__':
    main()
