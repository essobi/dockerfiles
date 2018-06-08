FROM ubuntu:15.04  
MAINTAINER Andrey Kuznetsov <fear@loathing.in>  
RUN apt-get update && \  
apt-get install --no-install-recommends -y software-properties-common && \  
apt-add-repository ppa:ansible/ansible && \  
apt-get update && \  
apt-get install -y ansible sudo  
  
RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts  

