from fabric.api import task, sudo, run

android_sdk_tgz = 'android-sdk_r23.0.2-linux.tgz'

@task
def font():
    sudo('yaourt -S --noconfirm ttf-vlgothic')

@task
def xfce4():
    sudo('pacman -Sy xfce4')

@task
def intellij():
    sudo('sudo pacman -Sy intellij-idea-community-edition')
    sudo('ln -sf /usr/lib/libgif.so.7.0.0 /usr/lib/libgif.so.6')

@task
def trouble_shoot():
    print('if you cannot use OpenJDK, try:')
    print('http://wiki.jetbrains.net/intellij/Installing_and_running_IntelliJ_IDEA_on_Ubuntu#Configuring_JDK_in_IntelliJ_IDEA')

@task
def android():
    run('wget http://dl.google.com/android/%s' % android_sdk_tgz)
    run('tar xf %s' % android_sdk_tgz)
    run("echo 'PATH=$PATH:$HOME/android-sdk-linux/tools' >> ~/.zshrc")
    print('run in X terminal: android update sdk')

@task
def all():
    '''
# intellij.all
font()
xfce4()
intellij()
trouble_shoot()
    '''
    exec(all.__doc__)
