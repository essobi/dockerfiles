FROM centos  
MAINTAINER Joseph M Jones  
ENV JAVA_HOME /usr/java/latest  
ENV JAVA_VERSION 8u60  
RUN curl -sLO --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}-b27/jdk-${JAVA_VERSION}-linux-x64.rpm  
RUN rpm -Uvh jdk-${JAVA_VERSION}-linux-x64.rpm && rm
jdk-${JAVA_VERSION}-linux-x64.rpm  

