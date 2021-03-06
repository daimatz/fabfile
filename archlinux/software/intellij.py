from fabric.api import task, sudo, run

android_sdk_tgz = 'android-sdk_r23.0.2-linux.tgz'
android_ndk_version = 'r9d'
android_ndk_base = 'android-ndk-%s' % android_ndk_version
android_ndk_tgz = '%s-linux-x86_64.tar.bz2' % android_ndk_base

@task
def font():
    sudo('yaourt -S --noconfirm ttf-vlgothic')

@task
def xfce4():
    sudo('pacman -Sy --noconfirm xfce4')

@task
def intellij():
    sudo('pacman -Sy --noconfirm intellij-idea-community-edition')
    sudo('ln -sf /usr/lib/libgif.so.7.0.0 /usr/lib/libgif.so.6')

@task
def trouble_shoot():
    print('if you cannot use OpenJDK, try:')
    print('http://wiki.jetbrains.net/intellij/Installing_and_running_IntelliJ_IDEA_on_Ubuntu#Configuring_JDK_in_IntelliJ_IDEA')

@task
def android_sdk():
    run('wget http://dl.google.com/android/%s' % android_sdk_tgz)
    run('tar xf %s' % android_sdk_tgz)
    run("echo 'export ANDROID_HOME=$HOME/android-sdk-linux' >> ~/.zshrc")
    run("echo 'export ANDROID_SDK_ROOT=$ANDROID_HOME' >> ~/.zshrc")
    run("echo 'export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools' >> ~/.zshrc")
    sudo('pacman -Sy --noconfirm gcc-multilib lib32-zlib lib32-ncurses lib32-readline')
    print('run in X terminal: android update sdk')

@task
def android_ndk():
    run('wget http://dl.google.com/android/ndk/%s' % android_ndk_tgz)
    run('tar xf %s' % android_ndk_tgz)
    run('mv %s android-ndk' % android_ndk_base)
    run("echo 'export NDK_ROOT=$HOME/android-ndk' >> ~/.zshrc")

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
