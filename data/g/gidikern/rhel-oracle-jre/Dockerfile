FROM registry.access.redhat.com/rhel7.1  
  
MAINTAINER Gidi Kern <gidikern@gmail.com>  
  
RUN curl -b oraclelicense=accept-securebackup-cookie -O -L
http://download.oracle.com/otn-pub/java/jdk/8u60-b27/jre-8u60-linux-x64.rpm &&
rpm -ivh jre-8u60-linux-x64.rpm && rm -rf jre-8u60-linux-x64.rpm  
  
ENV JAVA_HOME /usr/java/jre1.8.0_60  
  

