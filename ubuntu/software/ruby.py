from fabric.api import sudo, task, cd

@task
def install():
    with cd('/tmp'):
        sudo('git clone https://github.com/ruby/ruby.git')
    with cd('/tmp/ruby'):
        sudo('git checkout v2_1_0')
        sudo('autoconf')
        sudo('./configure')
        sudo('make')
        sudo('make install')

@task
def all():
    install()
