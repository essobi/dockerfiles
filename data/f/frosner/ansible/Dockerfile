FROM ubuntu:16.04  
  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
apt-get clean all -y  
RUN \  
add-apt-repository ppa:ansible/ansible && \  
apt-get update && \  
apt-get install -y ansible git && \  
apt-get clean all -y  
  
  

