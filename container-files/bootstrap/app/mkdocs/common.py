import os
from termcolor import colored
import git
from datetime import datetime
from crontab import CronTab

docks_dir = os.environ['DOCS_DIRECTORY']
modules = os.environ['ADD_MODULES']
repo = os.environ['GIT_REPO']
git_branch = os.environ['GIT_BRANCH']
auto_update = os.environ['AUTO_UPDATE']
interval = int(os.environ['UPDATE_INTERVAL'])


def start():
    """
    Start mkdocs server
    :return:
    """
    if modules != 'false':
        _install_modules(modules)
    if repo != 'false':
        _clone_repo(repo)
    _check_previous_installation()
    print('Starting MKDocs')
    os.chdir(docks_dir)
    os.system(f'mkdocs serve -a 0.0.0.0:8000 {_live_reload()} {_fast_mode()}')


def _install_modules(modules):
    """
    Install Additional Modules
    :param modules: str - List of modules to install
    :return:
    """
    print(colored(f'Installing python modules: {modules}', 'green'))
    os.system(f'pip install -q {modules}')
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
        os.system(f'mkdocs new {docks_dir}/')
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


def _set_auto_update(interval):
    """
    Creates cron job for auto updating repository
    :param interval: (every x minutes)
    :return:
    """
    os.system(f'crond')
    cron = CronTab(user='root')
    cron.remove_all()
    job = cron.new(command='bootstrap update', comment='update')
    job.minute.every(interval)
    cron.write()


def _clone_repo(repo):
    """
    Clone Documentation Code from git repository
    :return:
    """
    if not os.path.exists(docks_dir + '/mkdocs.yml'):
        print(colored(f'Getting documentation from: {repo}', 'green'))
        git.Repo.clone_from(repo, docks_dir, branch=git_branch)

    if auto_update == 'true':
        print(colored(f'AUTO_UPDATE - [ ENABLED ]', 'green'))
        print(colored(f'UPDATE_INTERVAL set to every {interval} minute/s', 'green'))
        _set_auto_update(interval)


def update_repo():
    """
    Fetching latest changes
    :return:
    """
    repo = git.Repo(docks_dir)
    for remote in repo.remotes:
        remote.fetch()
        remote.pull()
        headcommit = repo.head.commit
        commit_date = datetime.fromtimestamp(headcommit.authored_date)
        print(colored(
            f'Pulled branch: {git_branch} \nCommit: {headcommit.hexsha} \nCommit Message: {headcommit.message}Date: {commit_date} \nAuthor: {headcommit.committer.name}',
            'green'))
