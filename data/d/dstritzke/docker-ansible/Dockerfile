FROM ubuntu:15.10  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-add-repository ppa:ansible/ansible -y && \  
apt-get update && \  
apt-get install -y ssh=1:6.9p1-2ubuntu0.2 unzip=6.0-17ubuntu1.2
curl=7.43.0-1ubuntu2.1 ansible=2.2.0.0-1ppa~wily && \  
apt-get clean  

