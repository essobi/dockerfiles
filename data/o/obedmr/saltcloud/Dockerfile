FROM ubuntu:xenial  
MAINTAINER obed.n.munoz@gmail.com  
  
# Software Update  
RUN apt-get update -y  
RUN apt install software-properties-common curl gnupg2 locales alien openssh-
server samba-libs samba-dev smbclient python-pip -y  
RUN pip install --upgrade pip  
RUN pip install impacket  
  
# SaltCloud  
RUN curl -Ok
https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub  
RUN apt-key add SALTSTACK-GPG-KEY.pub  
RUN echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial
main" > /etc/apt/sources.list.d/saltstack.list  
RUN apt-get update -y  
RUN apt-get install salt-cloud salt-master salt-master salt-minion salt-ssh
salt-syndic salt-api python-novaclient -y  
  
RUN sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/g' /etc/locale.gen  
RUN locale-gen  
  
# Install extra utilities  
RUN apt-get install tmux curl -y  
  
# Install golang  
WORKDIR /usr/local  
RUN curl -Ok https://dl.google.com/go/go1.10.linux-amd64.tar.gz  
RUN tar -xzvf go1.10.linux-amd64.tar.gz  
RUN echo "PATH=$PATH:/usr/local/go/bin" > /root/.bashrc  
  
WORKDIR /root

