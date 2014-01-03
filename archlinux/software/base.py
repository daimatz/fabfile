from fabric.api import task, sudo, run

@task
def package():
    sudo('pacman -Sy --noconfirm base-devel tmux vim git tig zsh curl wget'
        ' sqlite zip unzip')
    sudo('yaourt -S --noconfirm nkf')
    sudo('ln -sf /usr/share/git/diff-highlight/diff-highlight /usr/bin')
    sudo('wget http://betterthangrep.com/ack-standalone -O /usr/bin/ack')
    sudo('chmod +x /usr/bin/ack')

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
dotfiles()
    '''
    exec(all.__doc__)
