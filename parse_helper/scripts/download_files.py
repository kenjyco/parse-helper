import click
import input_helper as ih
import parse_helper as ph


@click.command()
@click.argument('args', nargs=-1)
def main(args):
    """Download all links to local files

    - args: urls or filenames containing urls
    """
    urls = ih.get_all_urls(*args)
    session = ph.new_requests_session()
    for url in urls:
        ph.download_file(url, session=session)


if __name__ == '__main__':
    main()
