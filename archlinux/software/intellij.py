from fabric.api import task, sudo, run

@task
def xfce4():
    sudo('pacman -Sy xfce4')

@task
def intellij():
    sudo('sudo pacman -Sy intellij-idea-community-edition')
    sudo('ln -sf /usr/lib/libgif.so.7.0.0 /usr/lib/libgif.so.6')

@task
def all():
    '''
# intellij.all
xfce4()
intellij()
    '''
    exec(all.__doc__)
    print('if you cannot use OpenJDK, try:')
    print('http://wiki.jetbrains.net/intellij/Installing_and_running_IntelliJ_IDEA_on_Ubuntu#Configuring_JDK_in_IntelliJ_IDEA')
