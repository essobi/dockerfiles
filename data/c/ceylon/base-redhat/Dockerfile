#  
# Base image consisting of Fedora, Java 7, Ant, Maven and Git  
#  
FROM jboss/base-jdk:7  
  
MAINTAINER Tako Schotanus <tako@ceylon-lang.org>  
  
LABEL org.ceylon-lang.dockerfile.description="Base image consisting of Fedora,
Java 7, Ant, Maven and Git" \  
org.ceylon-lang.dockerfile.vendor="RedHat" \  
org.ceylon-lang.dockerfile.version="1.0"  
  
USER root  
  
RUN yum install -y git ant maven docbook2x sudo patch wget && \  
yum clean all  
  

