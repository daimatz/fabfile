from fabric.api import task, sudo, run

@task
def package():
    sudo('pacman -Sy --noconfirm base-devel tmux vim git mercurial tig zsh curl'
        ' wget sqlite zip unzip rsync the_silver_searcher hub ntp')
    sudo('yaourt -S --noconfirm nkf global jq')
    sudo('ln -sf /usr/share/git/diff-highlight/diff-highlight /usr/bin')
    sudo('ln -sf /usr/share/git/workdir/git-new-workdir /usr/bin')

@task
def locale():
    sudo('sed -i "s/#ja_JP.UTF-8/ja_JP.UTF-8/g" /etc/locale.gen')
    sudo('locale-gen')
    run('echo "export LANG=ja_JP.UTF-8" >> ~/.zshrc')

@task
def dotfiles():
    run('git clone --recursive git://github.com/daimatz/dotfiles')
    run('bash dotfiles/linker.sh')
    run('echo "source ~/.zsh/init.zsh" >> ~/.zshrc')
    sudo('chsh -s `which zsh` vagrant')

@task
def preexec_dhcpcd_n():
    run('echo "function dhcpcd-n() { sudo dhcpcd -n &> /dev/null }" >> ~/.zshrc')
    run('echo "add-zsh-hook preexec dhcpcd-n" >> ~/.zshrc')

@task
def fake_ntpd():
    run('echo "while :; do sudo ntpdate ntp.nict.jp; sleep 1000; done" > ~/.ntpd.sh')
    run('echo \'if [ -z "`psg .ntpd.sh`" ]; then nohup bash ~/.ntpd.sh &> /dev/null &; fi\' >> ~/.zshrc')

@task
def all():
    '''
# base.all
package()
locale()
dotfiles()
preexec_dhcpcd_n()
fake_ntpd()
    '''
    exec(all.__doc__)
