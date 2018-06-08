FROM centos:centos6  
MAINTAINER pierre.carre78@gmail.com <Pierre CARRE>  
  
# Install tar  
RUN yum -y install tar  
  
# Download JDK 7u65 from Oracle download site  
RUN cd /opt  
RUN curl -L 'http://download.oracle.com/otn-
pub/java/jdk/7u65-b17/jdk-7u65-linux-x64.tar.gz' -H 'Cookie:
oraclelicense=accept-securebackup-cookie; gpw_e24=Dockerfile' -o
jdk-7u65-linux-x64.tar.gz  
  
# Check md5 sum  
RUN echo 'c223bdbaf706f986f7a5061a204f641f jdk-7u65-linux-x64.tar.gz' >
jdk-7u65-linux-x64.tar.gz.md5  
RUN md5sum -c jdk-7u65-linux-x64.tar.gz.md5  
  
# Untar  
RUN tar -xzf jdk-7u65-linux-x64.tar.gz  
  
# Set JAVA_HOME  
ENV JAVA_HOME /opt/jdk1.7.0_65  
  
RUN ln -s /opt/jdk1.7.0_65/bin/* /usr/local/bin/

