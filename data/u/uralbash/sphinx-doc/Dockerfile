# Sphinx-doc  
#  
# VERSION 0.0.1  
# vi: set ft=dockerfile :  
FROM ubuntu:latest  
MAINTAINER Dmitry Svintsov <root@uralbash.ru>  
  
ENV HOME_USER vagrant  
ENV HOME_PASS 123  
## Update  
RUN apt-get update  
  
## SSH  
RUN apt-get install -y openssh-server && \  
mkdir /var/run/sshd && \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
## Install an SSH for Vagrant  
RUN mkdir -pm 700 $HOME/.ssh && \  
wget --no-check-certificate
'https://raw.github.com/mitchellh/vagrant/master/keys/vagrant.pub' -O
$HOME/.ssh/authorized_keys  
  
## Python  
RUN apt-get install -y python3-pip  
RUN pip3 install pip -U  
  
## Add USER  
RUN useradd -m -s /bin/bash ${HOME_USER} && \  
echo "${HOME_USER}:${HOME_PASS}"|chpasswd && \  
adduser ${HOME_USER} sudo && \  
echo ${HOME_USER}' ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
## Sphinx  
USER vagrant  
RUN pip3 install sphinx alabaster --user  
RUN echo "PATH=$HOME/.local/bin:$PATH" >> ~/.profile  
  
## Clean  
USER root  
RUN apt-get clean  
  
## Run sshd  
CMD ["/usr/sbin/sshd", "-D"]  
EXPOSE 22  
ONBUILD CMD ["/usr/sbin/sshd", "-D"]  
ONBUILD EXPOSE 22  

