FROM ubuntu:12.04  
RUN apt-get update  
  
# Install Ansible  
RUN apt-get -y install python-software-properties  
RUN apt-add-repository -y ppa:ansible/ansible  
RUN apt-get update  
RUN apt-get -y install ansible sudo  
  
# Install Ansible inventory file  
RUN if [ ! -d "/etc/ansible" ]; then mkdir /etc/ansible; fi  
RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts  

