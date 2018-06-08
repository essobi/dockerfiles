  
FROM centos:latest  
MAINTAINER garbanzo <garbanzo.info@gmail.com>  
RUN yum update -y  
RUN yum install -y vim  
  
# Java Setting  
RUN cd /tmp  
RUN yum install -y wget  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u102-b14/jdk-8u102-linux-x64.rpm  
RUN rpm -ivh jdk-8u102-linux-x64.rpm  
ENV JAVA_HOME /usr/java/default  
  
# Play Setting  
ADD ./play-1.2.5.4.01-java8 /opt/play  
ENV PATH $PATH:/opt/play/  
WORKDIR /app  
  

