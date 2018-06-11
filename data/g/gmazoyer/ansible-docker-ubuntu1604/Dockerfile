FROM ubuntu:xenial  
MAINTAINER Guillaume Mazoyer  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install requirements  
RUN apt-get update  
RUN apt-get install -y software-properties-common systemd  
RUN apt-get clean  
  
# Install Ansible  
RUN add-apt-repository -y ppa:ansible/ansible  
RUN apt-get update  
RUN apt-get install -y ansible  
RUN apt-get clean  
  
# Ansible inventory file  
RUN mkdir -p /etc/ansible/roles \  
&& echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts  

