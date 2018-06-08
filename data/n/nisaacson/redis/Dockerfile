# Redis  
#  
# VERSION 0.0.1  
# Use the Ubuntu base image provided by dotCloud  
FROM ubuntu:latest  
MAINTAINER Noah Isaacson clewfirst+docker@gmail.com  
  
# Update the APT cache  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install and setup project dependencies  
RUN apt-get install -y -qq python-software-properties  
RUN add-apt-repository -y ppa:chris-lea/redis-server  
RUN apt-get update -y  
  
# Install and setup project dependencies  
RUN apt-get install -y curl lsb-release supervisor openssh-server  
RUN apt-get install -y redis-server  
  
# Setup process management  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
# RUN locale-gen en_US en_US.UTF-8  
ADD ./etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Change ssh password  
RUN echo 'root:redis' | chpasswd  
  
RUN echo "ulimit -n 4096" >> /etc/default/redis  
  
# Hack for initctl  
# See: https://github.com/dotcloud/docker/issues/1024  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -s /bin/true /sbin/initctl  
  
# Expose default redis port and ssh port  
EXPOSE 6379 22  
# Run both the ssh server daemon and the redis-server via supervisord  
CMD ["/usr/bin/supervisord"]  

