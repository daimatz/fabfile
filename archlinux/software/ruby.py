from fabric.api import task, sudo

@task
def base():
    sudo('pacman -Sy --noconfirm ruby')
    sudo('gem i bundler pry rspec --no-user-install')

@task
def rails():
    sudo('pacman -Sy --noconfirm nodejs')
    sudo('gem i rails')

@task
def all():
    '''
# ruby.all
base()
rails()
    '''
    exec(all.__doc__)
