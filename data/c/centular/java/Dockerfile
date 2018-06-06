# java  
#  
# VERSION Java 8  
# use the centos base image provided by  
FROM centos:7  
MAINTAINER wessel Pieterse, wessel@ordercloud.com  
  
ENV JDK_VERSION 8u171  
ENV JDK_BUILD_VERSION b11  
  
# Upgrading system  
RUN yum -y upgrade ; yum clean all  
RUN yum -y install curl wget bash telnet; yum clean all  
  
ENV DOWNLOAD_LINK "http://download.oracle.com/otn-
pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.rpm"  
RUN curl -LO $DOWNLOAD_LINK -H 'Cookie: oraclelicense=accept-securebackup-
cookie' && rpm -i jdk-8u171-linux-x64.rpm; rm -f jdk-8u171-linux-x64.rpm; yum
clean all  
ENV JAVA_HOME /usr/java/default  
  
RUN yum install -y zlib fontconfig freetype libX11.x86_64 libXext.x86_64
libXrender.x86_64; yum clean all  

