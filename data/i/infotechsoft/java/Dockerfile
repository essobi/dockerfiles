# Docker file for cent-os with OpenJDK v7 JRE  
FROM centos:centos7  
  
MAINTAINER Ray Bradley "https://github.com/rmbrad"  
ENV JAVA_VERSION 1.7.0.151  
RUN yum -y install java-1.7.0-openjdk-headless-$JAVA_VERSION && \  
yum -y clean all  
  
ENV JAVA_HOME /usr/lib/jvm/jre  
  
CMD ["bash"]  

