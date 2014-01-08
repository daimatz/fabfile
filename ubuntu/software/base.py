from fabric.api import sudo, task

@task
def packages():
    sudo('apt-get update')
    sudo('apt-get install -y build-essential autoconf git vim zsh wget'
        ' tmux ruby1.9.1-full apt-transport-https bison flex')

@task
def all():
    packages()
