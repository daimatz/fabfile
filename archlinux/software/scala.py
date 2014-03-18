from fabric.api import task, sudo

@task
def scala_sbt():
    sudo('pacman -Sy --noconfirm jdk7-openjdk scala sbt')

@task
def all():
    '''
# scala_sbt.all
scala_sbt()
    '''
    exec(all.__doc__.strip())
