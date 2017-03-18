import click
import input_helper as ih
import parse_helper as ph


@click.command()
@click.argument('url', nargs=1, default='')
def main(url):
    """Create a soup object from a url and explore with pdb++"""
    url = url or ih.user_input('url')
    ph.soup_explore(url)


if __name__ == '__main__':
    main()
