from fabric.api import task, sudo

install_dir = '/usr'

@task
def ghc():
    sudo('pacman -Sy --noconfirm ghc')

@task
def cabal():
    sudo('pacman -Sy --noconfirm cabal-install')
    sudo('cabal update')
    sudo('cabal install cabal-install -j4 --prefix=%s' % install_dir)

@task
def dev_tools():
    sudo('pacman -Sy --noconfirm happy')
    sudo('cabal update')
    sudo('cabal install haskell-src-exts ghc-mod stylish-haskell doctest -j4 --prefix=%s' % install_dir)

@task
def all():
    '''
# haskell.all
ghc()
cabal()
dev_tools()
    '''
    exec(all.__doc__)
