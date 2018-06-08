####################################################################################  
# Creates a container with OpenJDK 8  
####################################################################################  
  
# Command reference:  
# docker build -t avanzabank/centos-openjdk8:0.0.1 -t avanzabank/centos-
openjdk8:latest .  
# docker run -it avanzabank/centos-openjdk8 /bin/bash  
  
  
FROM centos:7  
RUN yum -y install \  
curl \  
wget \  
java-1.8.0-openjdk-devel-1.8.0.151 \  
&& yum clean all  
  
ENV JAVA_HOME /etc/alternatives/java_sdk_1.8.0  
  
WORKDIR /opt  

