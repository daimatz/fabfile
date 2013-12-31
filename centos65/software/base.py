from fabric.api import task, sudo, settings

epel_rpm_url = 'http://ftp.iij.ad.jp/pub/linux/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm'

@task
def epel():
    with settings(warn_only=True):
        sudo('rpm -i %s' % epel_rpm_url)

@task
def install():
    sudo('yum install -y gcc make gcc-c++ zlib-devel openssl-devel'
        ' readline-devel sqlite-devel perl wget curl bind-utils file git mailx'
        ' man ntp openssh-clients patch rsync screen sysstat dstat htop'
        ' traceroute vim-enhanced libselinux-python unzip')

@task
def all():
    '''
# base.all
epel()
install()
    '''
    exec(all.__doc__.strip())
