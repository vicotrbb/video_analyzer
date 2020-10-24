import click
from modules import .

__author__ = 'Victor Bona'

@click.group()
def main():
    """
    Simple CLI to summarize videos, available on graphic interface as well.
    """
    pass


@main.command()
@click.option('--help', '-h')
def help():
    """
    Shows CLI tool help
    """
    pass


@main.command()
@click.argument('url')
@click.option('--source', '-s', type=String, default='youtube', show_default=True)
@click.option('--topics-len', '-t', type=int, default=3, show_default=True)
def summarize(url, source):
    click.echo("{}, {}".format(greeting, name))
