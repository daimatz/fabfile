from fabric.api import task, sudo, run

@task
def package():
    sudo('pacman -Sy --noconfirm base-devel tmux vim git mercurial tig zsh curl'
        ' wget sqlite zip unzip rsync the_silver_searcher hub')
    sudo('yaourt -S --noconfirm nkf')
    sudo('ln -sf /usr/share/git/diff-highlight/diff-highlight /usr/bin')

@task
def locale():
    sudo('sed -i "s/#ja_JP.UTF-8/ja_JP.UTF-8/g" /etc/locale.gen')
    sudo('locale-gen')

@task
def dotfiles():
    run('git clone --recursive git://github.com/daimatz/dotfiles')
    run('bash dotfiles/linker.sh')
    run('echo "source ~/.zsh/init.zsh" >> ~/.zshrc')
    sudo('chsh -s `which zsh` vagrant')

@task
def all():
    '''
# base.all
package()
locale()
dotfiles()
    '''
    exec(all.__doc__)
