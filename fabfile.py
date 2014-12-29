from __future__ import with_statement
from fabric.api import *
from fabric.colors import yellow
from fabric.colors import red
from fabric.contrib.console import confirm


def init_fab():
    """
    Initialize the file
    #"""
    env.user = 'ubuntu'

    # disable SSH strict host key checking
    env.disable_known_hosts = True
    env.hosts = [
            'eytan.us',
            ]

@task
@parallel
def git_pull(repo='/home/ubuntu/git/bwipjs'):
    """
    Update git repo
    """
    with cd(repo):
        sudo('git reset --hard HEAD && git pull', user='eytan')

@task
def deploy():
    git_pull()

init_fab()
