FROM ubuntu:16.04  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
## Repository  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 7BB9C367 &&\  
echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu xenial main" >
/etc/apt/sources.list.d/ansible.list  
  
## Packages  
RUN \  
apt-get update &&\  
apt-get install -y --no-install-recommends curl wget vim unzip ansible apt-
transport-https language-pack-en &&\  
rm -rf /var/lib/apt/lists/*  
  
## Locales  
RUN \  
locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8 LC_CTYPE=en_US.UTF-8  
  
## Environments  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:UTF-8  
ENV LC_ALL en_US.UTF-8  
CMD ["/bin/bash"]  

