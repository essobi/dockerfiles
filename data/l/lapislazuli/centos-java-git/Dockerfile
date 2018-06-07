FROM library/centos:7  
MAINTAINER Johann Egger <johann@codacy.com>  
  
#JAVA  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 31  
ENV JAVA_VERSION_BUILD 13  
ENV JAVA_PACKAGE jre  
  
RUN curl -kLOH "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie"\  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.rpm
&& rpm -i
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.rpm; rm
-f ${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}.rpm; yum -y
clean all  
  
ENV JAVA_HOME /usr/java/default  
  
# OTHER TOOLS  
RUN yum -y install curl unzip git; \  
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config; \  
yum -y clean all; \  
echo "[core]" >> ~/.gitconfig; \  
echo "quotepath = false" >> ~/.gitconfig;  

