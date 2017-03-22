import click
import input_helper as ih
import parse_helper as ph


@click.command()
@click.argument('args', nargs=-1)
def main(args):
    """Download all links to images

    - args: urls or filenames containing urls
    """
    urls = ih.get_all_urls(*args)
    for url in urls:
        ph.download_image(url)


if __name__ == '__main__':
    main()
