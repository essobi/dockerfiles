FROM centos:centos7.3.1611  
# Install useful packages  
RUN yum -y update && \  
yum -y install sudo openssh-server openssh-clients openssl-devel which tar m4  
  
WORKDIR /opt  
  
# Install JDK 8u131  
RUN curl http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm
-o java.rpm --cookie oraclelicense=accept-securebackup-cookie -L && \  
rpm -ivh java.rpm && \  
rm java.rpm  
  
# Download filebeat 5.5.2  
RUN curl
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.5.2-linux-x86_64.tar.gz
-o /tmp/filebeat.tar.gz  
  
# Unzip and install filebeat  
RUN tar zxf /tmp/filebeat.tar.gz -C /opt && mv
/opt/filebeat-5.5.2-linux-x86_64 /opt/filebeat && rm -rf /tmp/filebeat.tar.gz  

