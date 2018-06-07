# jmvrbanac/simple-keystone  
#  
# Docker image for running Keystone for development and testing ONLY  
#  
FROM ubuntu:latest  
MAINTAINER John Vrbanac <john.vrbanac@linux.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update; apt-get install -y keystone sqlite  
  
RUN mkdir -p /opt/docker_app  
COPY scripts /opt/docker_app/scripts  
  
RUN sh /opt/docker_app/scripts/setup.sh  
  
EXPOSE 5000 35357  
CMD ["/usr/bin/keystone-all"]

