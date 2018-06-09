FROM ubuntu:14.04  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
  
## Update repository  
RUN apt-get update  
  
## Install add-apt-repository  
RUN apt-get install -y --no-install-recommends software-properties-common  
  
## Add repository  
RUN \  
apt-add-repository ppa:ansible/ansible  
  
## Update and Upgrade all packages  
RUN \  
apt-get update && \  
apt-get dist-upgrade -y --no-install-recommends  
  
## Install packages  
RUN apt-get install -y --no-install-recommends curl wget ansible apt-
transport-https ca-certificates language-pack-en  
  
## Fix issue with Locale  
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8  
  
## Install scripts  
ADD files/ansible-build.py /usr/bin/ansible-build  
RUN \  
chmod a+x /usr/bin/ansible-build  
  
## Configure system  
COPY files/ansible_host /etc/ansible/hosts  
COPY files/ansible_conf /etc/ansible/ansible.cfg  
  
ADD run.py /sbin/docker-entrypoint  
RUN \  
mkdir -p etc/entrypoint.d/ && \  
chmod a+x /sbin/docker-entrypoint  
  
## Cleanup  
RUN \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/sbin/docker-entrypoint", "/bin/bash"]  
  

