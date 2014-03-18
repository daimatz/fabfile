from fabric.api import task, sudo

@task
def nodejs():
    sudo('pacman -Sy --noconfirm nodejs')

@task
def grunt():
    sudo('npm install -g grunt-cli')

@task
def all():
    '''
# nodejs.all
nodejs()
grunt()
    '''
    exec(all.__doc__.strip())
