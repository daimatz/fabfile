# -*- mode: ruby -*-
# vi: set ft=ruby

PRIVATE_KEY_PATH = '/tmp/droneio.pem'
File.open(PRIVATE_KEY_PATH, "w") { |f|
  f.puts(ENV['DRONE_IO_KEY'].gsub('|', "\n"))
}
File.chmod(0600, PRIVATE_KEY_PATH)

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "aws"
  config.vm.synced_folder "", "", disabled: true
  config.vm.provider :aws do |aws, override|
    aws.access_key_id     = ENV['AWS_ACCESS_KEY_ID']
    aws.secret_access_key = ENV['AWS_SECRET_ACCESS_KEY']
    aws.keypair_name = "drone.io"

    aws.instance_type = "t1.micro"
    aws.region = "us-west-2"

    aws.ami = "ami-d63e58e6"

    aws.security_groups = [ 'vagrant' ]
    aws.tags = { 'Name' => 'drone.io' }

    override.ssh.username = "ec2-user"

    override.ssh.private_key_path = PRIVATE_KEY_PATH
  end
end
