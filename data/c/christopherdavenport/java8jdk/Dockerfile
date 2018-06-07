# This is an implementation of the jdk8u74  
FROM centos:latest  
MAINTAINER Chris Davenport <ChristopherDavenport@outlook.com>  
  
RUN yum update -y && \  
yum install -y wget && \  
wget --no-check-certificate --no-cookies --head "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u92-b14/jdk-8u92-linux-x64.rpm && \  
yum localinstall -y jdk-8u92-linux-x64.rpm && \  
rm -f jdk-8u92-linux-x64.rpm && \  
yum clean all  
  
# Set Environmental Variables  
ENV JAVA_HOME /usr/java/jdk1.8.0_92  
ENV PATH ${PATH}:${JAVA_HOME}/bin  

