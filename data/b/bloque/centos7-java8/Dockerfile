############################################################  
# Image based on centos7 and oracle jdk8  
############################################################  
  
# Set the base  
FROM centos:centos7  
  
# File Author / Maintainer  
MAINTAINER Viswanath <a_bloque@yahoo.com>  
  
# Install Oracle JDK 8  
ENV JAVA_VERSION 8u151  
ENV JAVA_BUILD 8u151-b12  
ENV JAVA_DL_HASH e758a0de34e24606bca991d704f6dcbf  
  
RUN yum -y update && yum -y install wget tar nano && yum clean all  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/${JAVA_BUILD}/${JAVA_DL_HASH}/jdk-${JAVA_VERSION}-linux-x64.rpm"  
RUN yum localinstall -y jdk-8u151-linux-x64.rpm && rm -f ~/jdk*.rpm  
ENV JAVA_HOME /usr/java/jdk1.8.0_151/jre  
CMD ["bash"]

