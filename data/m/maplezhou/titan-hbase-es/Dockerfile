#  
# Base Java7 Centos7 Dockerfile  
#  
# Pull base image  
FROM centos:centos7  
  
# Install standard utils  
RUN yum -y install hostname tar unzip which && \  
yum clean all  
  
# Install Java7  
RUN curl -OL 'http://download.oracle.com/otn-
pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm' \  
-H 'Cookie: oraclelicense=accept-securebackup-cookie' && \  
rpm -i jdk-7u51-linux-x64.rpm && \  
rm jdk-7u51-linux-x64.rpm && \  
echo 'export JAVA_HOME=/usr/java/jdk1.7.0_51/' >> ~/.bashrc  
  
CMD ["echo", "base built"]  
  
# vim: set ts=4 sw=4 sts=4 ai et :  

