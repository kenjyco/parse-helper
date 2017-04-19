import click
import parse_helper as ph


@click.command()
@click.argument('url', nargs=1)
@click.argument('localfile', nargs=1, default='')
def main(url, localfile):
    """Download link to local file

    - url: a string
    - localfile: a string
    """
    ph.download_file(url, localfile)


if __name__ == '__main__':
    main()
