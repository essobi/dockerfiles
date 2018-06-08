FROM centos:centos7  
  
MAINTAINER Shameer Kunjumohamed <sameerean@gmail.com>  
  
RUN yum -y upgrade  
  
RUN yum -y update  
  
RUN yum -y install wget  
  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u102-b14/jdk-8u102-linux-x64.rpm  
  
RUN echo "1ffe998845b594c66db2703dd5f60d88 jdk-8u102-linux-x64.rpm" >> MD5SUM  
  
RUN md5sum -c MD5SUM  
  
RUN rpm -Uvh jdk-8u102-linux-x64.rpm  
  
RUN yum -y clean all  
  
RUN rm -f jdk-8u102-linux-x64.rpm MD5SUM  
  
ENV JAVA_HOME /usr/java/jdk1.8.0_102/jre  

