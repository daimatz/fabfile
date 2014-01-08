from fabric.api import sudo, task

@task
def lxc_docker():
    sudo('curl -s https://get.docker.io/ubuntu/ | sudo sh')

@task
def all():
    lxc_docker()
