FROM centos:6.6  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
RUN yum update -y  
RUN yum install -y wget && wget --no-check-certificate --no-cookies --header
"Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/7u75-b13/jdk-7u75-linux-x64.rpm  
RUN rpm -ivh jdk-7u75-linux-x64.rpm && rm jdk-7u75-linux-x64.rpm  
  
ENV JAVA_HOME=/usr/java/jdk1.7.0_75  

