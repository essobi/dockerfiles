# Latest Ubuntu LTS  
FROM ubuntu:16.04  
  
# Ansible requirements  
RUN apt-get update -qq  
RUN apt-get install -y software-properties-common python-software-properties  
  
# Ansible installation  
RUN apt-add-repository -y ppa:ansible/ansible  
RUN apt-get update -qq  
RUN apt-get install -y ansible  
  
# Other tools  
RUN apt-get install -y rsync  

