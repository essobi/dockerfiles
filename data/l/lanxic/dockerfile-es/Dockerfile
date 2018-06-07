# Dockerfile to build Elasticsearch in container images  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
# File Author / Maintainer  
MAINTAINER Alex lanxic@gmail.com  
# set env with noninteractive  
ENV DEBIAN_FRONTEND=noninteractive  
# Update the repository sources list  
RUN apt-get update -y  
  
# install auditional tools build-essential  
RUN apt-get install -y wget vim curl openssh-server  
  
# Create the default data directory  
RUN mkdir -p /root/.ssh && chmod 0700 /root/.ssh  
COPY files/authorized_keys /root/.ssh/authorized_keys  
  
# initialing user and group ubuntu  
RUN groupadd -g 1000 ubuntu  
RUN useradd -u 1000 -g 1000 -d /home/ubuntu -m ubuntu -s /bin/bash  
RUN mkdir -p /home/ubuntu/.ssh && chmod 0700 /home/ubuntu/.ssh  
COPY files/authorized_keys /home/ubuntu/.ssh/authorized_keys  
RUN chown -R ubuntu: /home/ubuntu/.ssh/ -f  
  
# initialing user and group git  
RUN groupadd -g 10000 git  
RUN useradd -u 10000 -g 10000 -d /home/git -m git -s /bin/bash  
RUN mkdir -p /home/git/.ssh && chmod 0700 /home/git/.ssh  
COPY files/authorized_keys /home/git/.ssh/authorized_keys  
RUN chown -R git: /home/git/.ssh/ -f  
  
# initiling group admins  
RUN groupadd admins  
RUN usermod -aG admins ubuntu  
COPY files/sudo_admins /etc/sudoers.d/admins  
  
################## BEGIN INSTALLATION ######################  
# Install Elasticsearch Gotomalls Following the Instructions at Elasticsearch
Docs  
# Ref:  
# Add the package verification key and install java environment  
RUN apt-get update -y  
RUN apt-get install -y htop awscli  
  
RUN wget --quiet --header 'Cookie: oraclelicense=accept-securebackup-cookie'
http://download.oracle.com/otn-
pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.tar.gz
-O /tmp/jdk-8u121-linux-x64.tar.gz  
RUN tar -xf /tmp/jdk-8u121-linux-x64.tar.gz -C /opt  
RUN ln -s /opt/jdk1.8.0_121/ /opt/java  
  
RUN groupadd elasticsearch  
RUN useradd -d /opt/elasticsearch -s /bin/false -g elasticsearch elasticsearch  
RUN wget --quiet
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.3/elasticsearch-2.3.3.tar.gz
-O /tmp/elasticsearch-2.3.3.tar.gz  
RUN tar -xf /tmp/elasticsearch-2.3.3.tar.gz -C /opt  
RUN ln -s /opt/elasticsearch-2.3.3 /opt/elasticsearch  
COPY files/elasticsearch_yml /opt/elasticsearch/config/elasticsearch.yml  
RUN chown -R elasticsearch:elasticsearch /opt/elasticsearch/ -f  
  
RUN mkdir -p /var/elasticsearch/data  
RUN mkdir -p /var/elasticsearch/snapshot  
RUN chown -R elasticsearch: /var/elasticsearch/ -f  
COPY files/elasticsearch_init /etc/init/elasticsearch.conf  
  
##################### INSTALLATION END #####################  
  
# Set default container command  
COPY files/start.sh /start.sh  
ENTRYPOINT /bin/sh /start.sh  

