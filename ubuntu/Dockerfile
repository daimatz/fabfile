FROM ubuntu:12.04

ENV USER dai

RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -s /bin/true /sbin/initctl

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y vim passwd openssh-client openssh-server sudo

## create user
RUN useradd $USER -d /home/$USER -m
RUN echo $USER:$USER | chpasswd

## setup sudoers
RUN echo "$USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USER
RUN chmod 440 /etc/sudoers.d/$USER

## setup sshd and generate ssh-keys by init script
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g' /etc/ssh/sshd_config
RUN sed -i 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -i 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config
RUN /etc/init.d/ssh start
RUN /etc/init.d/ssh stop

CMD mkdir /var/run/sshd; /usr/sbin/sshd -D

# run with
#   $ docker port $(docker run -d -p 22 image_name) 22
# to run the VM and see what port number have mapped.
