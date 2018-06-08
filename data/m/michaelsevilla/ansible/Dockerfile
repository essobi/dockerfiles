FROM tutum/ubuntu:trusty  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
RUN echo "===> Install the basics..." && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
echo "===> Install Ansible..." && \  
sudo apt-get install -y python-setuptools python-dev build-essential libssl-
dev && \  
sudo easy_install pip && \  
sudo pip install ansible==2.1.2.0 && \  
echo "===> Cleanup apt-get..." && \  
sudo apt-get clean && sudo rm -rf \  
/var/lib/apt/lists/* /etc/apt/sources.list.d/ansible.list \  
tmp/* /var/tmp/*  
  
ENV "TERM=xterm-256color"  
ENTRYPOINT ["/usr/local/bin/ansible-playbook"]  

