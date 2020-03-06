from app.mkdocs.command import Command
import os
from termcolor import colored

docks_dir = os.environ['DOCS_DIRECTORY']


def start():
    """
    Start mkdocs server
    :return:
    """
    _check_previous_installation()
    print('Starting MKDocs')
    Command(f'mkdocs serve -a 0.0.0.0:8000 {_live_reload()} {_fast_mode()}').run()


def install_modules(modules):
    """
    Install Additionale Modules
    :param modules: str - Lust of modules to install
    :return:
    """
    print(f'Installing python modules: {modules}')
    Command(f'pip install -q {modules}')
    print(colored(f'Modules installed.', 'green'))


def _check_previous_installation():
    """
    Check if previous installation present
    Creates empty documentation if none detected
    :return:
    """
    if not os.path.exists(docks_dir + '/mkdocs.yml'):
        print(colored(f'No documentation found in ({docks_dir}). Creating new one.', 'yellow'))
        if not os.path.exists(docks_dir):
            os.mkdir(docks_dir)
        print(colored(f'Starting fresh installation', 'green'))
        Command(f'mkdocs new {docks_dir}/').run()
    else:
        print(colored(f'Detected previous installation in ({docks_dir}).', 'green'))


def _live_reload():
    """
    Live Reload
    Auto Reload on file change
    :return:
    """
    if os.environ['LIVE_RELOAD_SUPPORT'] == 'false':
        print(colored(f'LIVE RELOAD - [ DISABLED ]', 'red'))
        reload = '--no-livereload'
    else:
        print(colored(f'LIVE RELOAD - [ ENABLED ]', 'green'))
        reload = ''
    return reload


def _fast_mode():
    """
    Fast Mode
    Enables/Disables fast reload.
    Enabled: build only files that got changed
    Disabled: builds all files regardless of changes
    :return:
    """
    if os.environ['FAST_MODE'] == 'false':
        print(colored(f'FAST_MODE - [ DISABLED ]', 'red'))
        fast = ''
    else:
        print(colored(f'FAST_MODE - [ ENABLED ]', 'green'))
        fast = '--dirtyreload'
    return fast
