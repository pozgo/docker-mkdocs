from typing import Callable
from app.mkdocs import common
import click
import os

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
    modules = os.environ['ADD_MODULES']
    if modules != 'false':
        common.install_modules(modules)
    common.start()
