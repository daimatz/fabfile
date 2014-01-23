from fabric.api import sudo, task

@task
def kernel_update():
    sudo('apt-get update')
    sudo('apt-get dist-upgrade -y')
    sudo('apt-get install -y linux-image-generic-lts-raring'
        ' linux-headers-generic-lts-raring')
    sudo('reboot')

