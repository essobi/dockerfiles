FROM ubuntu:14.04  
  
ENV VERSION "0.25.0-0.2.70.ubuntu1404"  
  
MAINTAINER Container Solutions BV <info@container-solutions.com>  
  
RUN echo "deb http://ppa.launchpad.net/openjdk-r/ppa/ubuntu trusty main" >
/etc/apt/sources.list.d/openjdk.list && \  
echo "deb http://repos.mesosphere.io/ubuntu/ trusty main" >
/etc/apt/sources.list.d/mesosphere.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv 86F44E2A && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv E56151BF && \  
apt-get update && \  
apt-get -y install openjdk-8-jre-headless mesos curl && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -so /usr/bin/docker
https://get.docker.com/builds/Linux/x86_64/docker-1.8.3 && chmod +x
/usr/bin/docker  

