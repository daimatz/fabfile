from fabric.api import task, sudo

@task
def erlang():
    sudo('pacman -Sy --noconfirm erlang')

@task
def all():
    '''
# erlang.all
erlang()
    '''
    exec(all.__doc__)
