FROM centos:7  
MAINTAINER Mario Mohr <mohr.mario@gmail.com>  
  
ENV JAVA_VERSION 8u162  
ENV BUILD_VERSION b12  
ENV DOWNLOAD_LINK "http://download.oracle.com/otn-
pub/java/jdk/8u162-b12/0da788060d494f5095bf8624735fa2f1/jre-8u162-linux-x64.rpm"  
# Upgrading system  
RUN yum -y update && \  
yum -y install wget && \  
wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=xxx;
oraclelicense=accept-securebackup-cookie" "$DOWNLOAD_LINK" -O
/tmp/jre-8-linux-x64.rpm && \  
yum -y install /tmp/jre-8-linux-x64.rpm && \  
rm -f /tmp/jre-8-linux-x64.rpm && \  
yum clean all  
  
ENV JAVA_HOME /usr/java/latest  

