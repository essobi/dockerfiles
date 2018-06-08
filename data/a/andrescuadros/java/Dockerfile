FROM centos:7  
MAINTAINER Andres Cuadros "andrescuadros@gmail.com"  
  
ENV JAVA_VERSION=8u101 BUILD_VERSION=b13 JAVA_HOME=/usr/java/latest  
  
## Installing java:  
# - Install wget  
# - Download java rpm  
# - Install java rpm  
# - Set java commands with alternatives  
# - Remove java rpm  
RUN yum -y install wget \  
&& wget \--no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" -O
/tmp/jdk-8-linux-x64.rpm \  
&& yum -y install /tmp/jdk-8-linux-x64.rpm \  
&& alternatives \--install /usr/bin/java java /usr/java/latest/bin/java 1 \  
&& alternatives \--install /usr/bin/javaws javaws /usr/java/latest/bin/javaws
1 \  
&& alternatives \--install /usr/bin/javac javac /usr/java/latest/bin/javac 1 \  
&& rm /tmp/jdk-8-linux-x64.rpm  

