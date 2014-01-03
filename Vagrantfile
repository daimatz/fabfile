# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "aws"
  config.vm.synced_folder "", "", disabled: true
  config.vm.provider :aws do |aws, override|
    aws.access_key_id     = ENV['AWS_ACCESS_KEY_ID']
    aws.secret_access_key = ENV['AWS_SECRET_ACCESS_KEY']
    aws.keypair_name = "drone.io"

    aws.instance_type = "c1.medium"
    aws.region = "us-west-2"

    aws.ami = "ami-d63e58e6"

    aws.security_groups = [ 'vagrant' ]
    aws.tags = { 'Name' => 'drone.io' }

    override.ssh.username = "ec2-user"

    override.ssh.private_key_path = ENV['PRIVATE_KEY_FILE']
  end
end
