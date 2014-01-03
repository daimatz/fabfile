# vagrant
git clone git://github.com/mitchellh/vagrant.git
cd vagrant
git checkout refs/tags/v1.4.0
bundle install
rake install

# vagrant-aws
vagrant plugin install vagrant-aws
vagrant box add aws https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box
vagrant up --provider=aws
mkdir -p ~/.ssh
vagrant ssh-config --host=ec2 > ~/.ssh/config

# fabric
sudo apt-get update
sudo apt-get install python-setuptools
sudo easy_install fabric

# run fabric
cd centos65
fab --set=use_ssh_config=True -H ec2 all

# run serverspec

# destroy instance
cd ..
vagrant destroy -f
