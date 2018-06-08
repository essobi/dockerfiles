FROM ping2ravi/ubuntu:14.04  
MAINTAINER Ravi Sharma  
  
  
# Oracle Java Version 8  
ENV JAVA_VERSION 8  
ENV JAVA_UPDATE 65  
ENV JAVA_BUILD 17  
ENV JAVA_FILE_NAME=jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64  
  
ENV JAVA_HOME /opt/java/java-${JAVA_VERSION}  
  
  
RUN sudo su; apt-get update; apt-get install unzip ; apt-get install gzip ;
apt-get -y install wget  
  
RUN sudo su; wget --no-cookies --header "Cookie: oraclelicense=xxx;"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/${JAVA_FILE_NAME}.tar.gz
; gunzip ${JAVA_FILE_NAME}.tar.gz ; tar -xvf ${JAVA_FILE_NAME}.tar ; rm
${JAVA_FILE_NAME}.tar ; mkdir -p ${JAVA_HOME} ; mv
jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}/* ${JAVA_HOME} ; rm -fR
jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE};  
  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  

