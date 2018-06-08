FROM centos:7  
  
ENV \  
JAVA_VERSION=8u111 \  
BUILD_VERSION=b14  
  
RUN \  
curl -s -L -H "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/java.rpm \  
"http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" &&
\  
yum -y install /tmp/java.rpm && \  
yum clean all && \  
rm -f /tmp/java.rpm  
  
ENV JAVA_HOME=/usr/java/default  

