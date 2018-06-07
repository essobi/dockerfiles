FROM centos:centos6  
MAINTAINER Ingensi labs <contact@ingensi.com>  
  
RUN yum update -y  
RUN yum install -y wget && wget --no-check-certificate --no-cookies --header
"Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u11-b12/jdk-8u11-linux-x64.rpm  
RUN rpm -ivh jdk-8u11-linux-x64.rpm && rm jdk-8u11-linux-x64.rpm  

