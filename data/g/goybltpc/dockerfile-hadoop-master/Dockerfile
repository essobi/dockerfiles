# Version 0.0.1  
FROM centos:centos6  
MAINTAINER Wu Weiwei "iphone1945@126.com-master"  
  
RUN yum install openssh-server -y && \  
yum install openssh-clients -y && \  
service sshd start && \  
chkconfig sshd on && \  
mkdir mydir && cd /opt && \  
curl -O https://archive.cloudera.com/cdh5/cdh/5/hadoop-2.6.0-cdh5.4.0.tar.gz
&& \  
tar -xzvf hadoop-2.6.0-cdh5.4.0.tar.gz && \  
JAVA_VERSION_MAJOR=8 && \  
JAVA_VERSION_MINOR=131 && \  
JAVA_VERSION_BUILD=11 && \  
JAVA_PACKAGE=jdk && \  
cd /opt && \  
curl -jkSLH "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/d54c1d3a095b4ff2b6607d096fa80163/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
|tar -xzf - -C . && \  
JDK_PATH=jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}  
  
  
  
  
EXPOSE 80  

