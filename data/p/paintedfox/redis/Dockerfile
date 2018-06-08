# Redis (http://redis.io/)  
FROM ubuntu:precise  
MAINTAINER Ryan Seto <ryanseto@yak.net>  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
# Prevent apt-get from complaining with: Unable to connect to Upstart  
RUN dpkg-divert --local --rename --add /sbin/initctl && \  
ln -s /bin/true /sbin/initctl  
  
RUN apt-get install -y python-software-properties && \  
apt-add-repository -y ppa:rwky/redis && \  
apt-get update  
  
RUN apt-get install -y redis-server  
  
ENTRYPOINT ["/usr/bin/redis-server"]  

