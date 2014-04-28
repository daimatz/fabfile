from fabric.api import task, sudo, cd, run

eclipse_tgz = 'eclipse-SDK-4.3.2-linux-gtk-x86_64.tar.gz'
eclipse_url = 'http://ftp.jaist.ac.jp/pub/eclipse/eclipse/downloads/drops4/R-4.3.2-201402211700/%s' % eclipse_tgz
eclim_version = '2.3.2'
eclim_jar = 'eclim_%s.jar' % eclim_version
eclim_url = 'http://jaist.dl.sourceforge.net/project/eclim/eclim/%s/%s' % (eclim_version, eclim_jar)

@task
def dependencies():
    sudo('pacman -Sy --noconfirm xorg-server-xvfb libcups nvidia-libgl gtk2'
        ' libxtst')
    sudo('yaourt -S --noconfirm ttf-vlgothic')

@task
def eclipse():
    run('wget %s' % eclipse_url)
    run('tar xf %s' % eclipse_tgz)

@task
def eclim():
    run('wget %s' % eclim_url)

@task
def sshd_config():
    sudo('sed -ri "s/#X11Forwarding no/X11Forwarding yes/g" /etc/ssh/sshd_config')
    sudo('systemctl restart sshd')

@task
def message():
    print('Eclim installation requires X.')
    print('1. Reboot the machine.')
    print('2. Login with `ssh -X` and run `java -jar %s`.' % eclim_jar)

@task
def all():
    '''
# eclim.all
Xvfb()
font()
libgl()
eclipse()
eclim()
sshd_config()
message()
    '''
    exec(all.__doc__)
