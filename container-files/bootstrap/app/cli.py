import click
from app.mkdocs import common

"""CLI commands interface

    These are the primitive operation wrappers that the CLI
    will expose and be available to invoke.
    In order to do so, the comprehensive Click library is used to
    create commands, subcommands, parameters, flags...

    .. _Click CLI library docs:
        https://click.palletsprojects.com/en/7.x/#documentation
"""


@click.group(chain=True)
def cli() -> None:
    """
    Bootstrap CLI
    """


@cli.command('start', help='Start Application')
def start():
    common.start()


@cli.command('update', help='Update documentation code from repository')
def update():
    common.update_repo()
