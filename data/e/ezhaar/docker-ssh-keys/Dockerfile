# Build hadoo-base image on Ubuntu 14.04.1  
FROM ubuntu:14.04.1  
MAINTAINER Izhar ul Hassan "ezhaar@gmail.com"  
USER root  
  
RUN apt-get update && apt-get install -y \  
openssh-client  
RUN rm -rf /var/lib/apt/lists/*  
VOLUME /root/.ssh  
CMD ssh-keygen -q -t rsa -P '' -f /root/.ssh/id_rsa && cat
/root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys  
  

