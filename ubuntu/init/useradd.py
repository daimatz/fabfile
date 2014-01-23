from fabric.api import sudo, task, put

user = 'dai'
github_user_id = 'daimatz'

@task
def useradd_ssh_config():
    sudo('apt-get update')
    sudo('apt-get install -y curl passwd')
    sudo('echo 127.0.1.1 `hostname` >> /etc/hosts')
    sudo('useradd %s -d /home/%s -m' % (user, user))
    # sudo('echo %s:%s | chpasswd' % (user, user))
    sudo('echo "%s ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/%s' % (user, user))
    sudo('chmod 440 /etc/sudoers.d/%s' % user)
    sudo('mkdir -p /home/%s/.ssh' % user)
    sudo('curl https://github.com/%s.keys > /home/%s/.ssh/authorized_keys'
        % (github_user_id, user))
    sudo('chmod 700 /home/%s/.ssh' % user)
    sudo('chmod 600 /home/%s/.ssh/authorized_keys' % user)
    sudo('chown -R %s:%s /home/%s/.ssh' % (user, user, user))
    put('template/etc/ssh/sshd_config', '/etc/ssh/sshd_config', use_sudo=True)
    sudo('service ssh restart')
