FROM maven:3-jdk-8  
MAINTAINER Torsten Walter  
  
RUN apt-get update -y  
RUN apt-get install -y apt-transport-https ca-certificates  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list  
RUN apt-get update  
RUN apt-cache policy docker-engine  
  
RUN apt-get update  
RUN apt-get install -y docker-engine  

