from fabric.api import task, sudo, cd

cache_dir = '/var/cache'

ghc_version = '7.6.3'
ghc_source = 'ghc-%s-src.tar.bz2' % ghc_version
ghc_source_url = 'http://www.haskell.org/ghc/dist/%s/%s' % (ghc_version, ghc_source)

cabal_version = 'Cabal-v1.18.1.2'
cabal_source = '%s.tar.gz' % cabal_version
cabal_source_url = 'https://github.com/haskell/cabal/archive/%s' % cabal_source

@task
def dependencies():
    sudo('apt-get install -y ghc libgmp-dev libgmp3-dev zlib1g-dev ncurses-dev'
        ' happy alex')

@task
def download_ghc_source():
    sudo('wget %s -O %s/%s' % (ghc_source_url, cache_dir, ghc_source))

@task
def unarchive_ghc_source():
    with cd(cache_dir):
        sudo('tar xf %s' % ghc_source)

@task
def install_ghc():
    with cd('%s/ghc-%s' % (cache_dir, ghc_version)):
        sudo('./configure --prefix=/usr')
        sudo('make')
        sudo('make install')

@task
def download_cabal_source():
    sudo('wget %s -O %s/%s' % (cabal_source_url, cache_dir, cabal_source))

@task
def unarchive_cabal_source():
    with cd(cache_dir):
        sudo('tar xf %s' % cabal_source)

@task
def install_cabal():
    with cd('%s/cabal-%s/cabal-install' % (cache_dir, cabal_version)):
        sudo('PREFIX=/usr ./bootstrap.sh')

@task
def all():
    '''
# haskell.all
dependencies()
download_ghc_source()
unarchive_ghc_source()
install_ghc()
download_cabal_source()
unarchive_cabal_source()
install_cabal()
    '''
    exec(all.__doc__.strip())
