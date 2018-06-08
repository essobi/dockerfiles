# Dockerfile for an openvswitch container on CoreOS.  
FROM shift/coreos-ubuntu-confd:latest  
  
MAINTAINER Vincent Palmer <shift-gh@someone.section.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install openvswitch-switch -y  

