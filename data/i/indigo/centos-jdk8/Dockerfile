FROM centos:7  
MAINTAINER ronny@no42.org  
  
ENV JAVA_VERSION 8u121  
ENV JAVA_BUILD b13  
ENV JAVA_HOME /usr/java/jdk1.8.0_121  
  
RUN curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}-${JAVA_BUILD}/e9e7ea248e2c4826b92b3f075a80e441/jdk-${JAVA_VERSION}-linux-x64.rpm
> /tmp/jdk-linux-x64.rpm && \  
yum -y install /tmp/jdk-linux-x64.rpm && \  
rm /tmp/jdk-linux-x64.rpm && \  
yum clean all  

