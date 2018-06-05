# debian wheezy + java 7u79  
#  
# VERSION 0.0.6  
# 0.0.1 : initial file with centos 6.4 and java 7u60  
# 0.0.2 : change centos from 6.4 to 6 and java 7u60 to 7u71  
# 0.0.3 : take only necessary in jdk (jre+tools.jar) : reduce image size from
580.4MB to 449.6MB, add JAVA_HOME env  
# 0.0.4 : change to debian:wheezy in order to reduce image size
(449.6MB->269.4MB)  
# 0.0.5 : add unzip package + update to 7u79  
# forked repository from snasello/docker-debian-java7  
# 0.0.6 : use full JDK instead of jre  
  
FROM debian:wheezy  
  
MAINTAINER Ayoub Boulila <ayoubboulila@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y curl tar unzip \  
&& (curl -s -k -L -C - -b "oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.tar.gz
| tar xfz - -C /opt) \  
&& ln -s /opt/jdk1.7.0_79 /opt/java  
  
# Set JAVA_HOME  
ENV JAVA_HOME /opt/java  

