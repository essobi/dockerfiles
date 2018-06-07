# This is an implementation of the jdk7u79  
FROM centos:latest  
MAINTAINER Chris Davenport <ChristopherDavenport@outlook.com>  
  
RUN yum update -y && \  
yum install -y wget && \  
wget --no-check-certificate --no-cookies --head "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/7u79-b15/jdk-7u79-linux-x64.rpm && \  
yum localinstall -y jdk-7u79-linux-x64.rpm && \  
rm -f jdk-7u79-linux-x64.rpm && \  
yum clean all  
  
# Set Environmental Variables  
ENV JAVA_HOME /usr/java/jdk1.7.0_79  
ENV PATH ${PATH}:${JAVA_HOME}/bin  

