from fabric.api import task, sudo, cd

install_dir_prefix = '/usr/cabal'
symlink_bindir = '/usr/bin'
install_command = 'cabal install -j4 --symlink-bindir=%s %s %s'

def cabal_install_executable(packages, other_option=''):
    for package in packages:
        sudo('mkdir -p %s/%s' % (install_dir_prefix, package))
        with cd('%s/%s' % (install_dir_prefix, package)):
            sudo('cabal sandbox init')
            sudo('cabal update')
            sudo(install_command % (symlink_bindir, other_option, package))

@task
def ghc():
    sudo('pacman -Sy --noconfirm ghc')

@task
def cabal():
    sudo('pacman -Sy --noconfirm cabal-install')
    sudo('cabal update')
    sudo('cabal install -j4 --prefix=/usr cabal-install')
    cabal_install_executable(['cabal-install'])

@task
def dev_tools():
    sudo('pacman -Sy --noconfirm happy alex')
    cabal_install_executable(['ghc-mod', 'stylish-haskell', 'doctest'])

@task
def mighttpd():
    cabal_install_executable(['mighttpd2'])

@task
def all():
    '''
# haskell.all
ghc()
cabal()
dev_tools()
    '''
    exec(all.__doc__)
