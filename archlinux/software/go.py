from fabric.api import task, sudo, run

go_version = '1.3'
go_source = 'go%s.linux-amd64.tar.gz' % go_version
go_url = 'http://golang.org/dl/%s' % go_source

goroot = '$HOME/.goroot'
gopath = '$HOME'

@task
def go():
    run('wget %s' % go_url)
    run('tar xf %s' % go_source)
    run('rm %s' % go_source)
    run("mv go %s" % goroot)

@task
def set_goroot_gopath():
    run("echo 'export GOROOT=%s' >> ~/.zshrc" % goroot)
    run("echo 'export GOPATH=%s' >> ~/.zshrc" % gopath)
    run("echo 'export PATH=$PATH:$GOROOT/bin:$GOPATH/bin' >> ~/.zshrc")

@task
def dev_tools():
    for i in [
        'code.google.com/p/go.tools/cmd/goimports',
        'code.google.com/p/go.tools/cmd/godoc',
        'code.google.com/p/go.tools/cmd/vet',
        'code.google.com/p/go.tools/cmd/cover',
        'github.com/nsf/gocode',
        'github.com/lestrrat/peco/cmd/peco',
        'github.com/motemen/ghq',
    ]:
        run('GOROOT=%s GOPATH=%s %s/bin/go get %s' % (goroot, gopath, goroot, i))

@task
def all():
    '''
# go.all
go()
set_goroot_gopath()
dev_tools()
    '''
    exec(all.__doc__)
