FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:ansible/ansible && \  
apt-get update && \  
apt-get install -y openssh-client rsync sshpass ansible && \  
apt-get purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  

