FROM centos:7  
MAINTAINER Carlos Feliz <carlos@spiffylogic.com>  
ENV REFRESHED_AT 03-18-2016  
RUN yum update -y -q && \  
yum install -y -q epel-release && \  
yum repolist -y -q && \  
yum install -y sshpass && \  
yum install -y git && \  
yum install -y gcc && \  
yum install -y python-setuptools && \  
easy_install pip && \  
yum install -y python-paramiko && \  
pip install ansible  

