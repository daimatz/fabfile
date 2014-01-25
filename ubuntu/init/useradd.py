from fabric.api import sudo, task, put, settings, cd

user = 'dai'
github_user_id = 'daimatz'

import os
template_dir = os.path.dirname(__file__) + '/../template'

@task
def useradd_ssh_config():
    sudo('apt-get update')
    sudo('apt-get install -y curl')
    with settings(warn_only=True):
        if sudo('grep 127.0.1.1 /etc/hosts').failed:
            sudo('echo 127.0.1.1 `hostname` >> /etc/hosts')
        if sudo('grep ^%s /etc/passwd' % user).failed:
            sudo('useradd %s -d /home/%s -m' % (user, user))
    sudo('echo "%s ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/%s' % (user, user))
    sudo('chmod 440 /etc/sudoers.d/%s' % user)
    with settings(sudo_user=user):
        sudo('mkdir -p /home/%s/.ssh' % user)
        sudo('curl https://github.com/%s.keys > /home/%s/.ssh/authorized_keys'
            % (github_user_id, user))
        sudo('chmod 700 /home/%s/.ssh' % user)
        sudo('chmod 600 /home/%s/.ssh/authorized_keys' % user)
    put('%s/etc/ssh/sshd_config' % template_dir, '/etc/ssh/sshd_config',
        use_sudo=True)
    sudo('service ssh restart')

@task
def dotfiles():
    with settings(sudo_user=user):
        with cd('/home/%s' % user):
            sudo('git clone --recursive git://github.com/%s/dotfiles'
                % github_user_id)
            sudo('bash ~/dotfiles/linker.sh')
            sudo('echo "source ~/.zsh/init.zsh" >> ~/.zshrc')
    sudo('chsh -s `which zsh` %s' % user)
