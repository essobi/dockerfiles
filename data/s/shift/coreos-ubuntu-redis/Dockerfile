# Dockerfile for a Redis container on CoreOS.  
FROM shift/coreos-ubuntu-confd:latest  
  
MAINTAINER Vincent Palmer <shift-gh@someone.section.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y python-software-properties  
RUN add-apt-repository -y ppa:rwky/redis  
RUN apt-get update  
RUN apt-get install -y redis-server  
RUN apt-get -y install redis-server  
ADD files/run.sh /run.sh  
RUN chmod 0755 /run.sh  
EXPOSE 6379  

