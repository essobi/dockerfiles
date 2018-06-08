FROM centos:6  
  
RUN \  
curl -s -L -C - -b "oraclelicense=accept-securebackup-cookie" -o /tmp/java.rpm
\  
"http://download.oracle.com/otn-
pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.rpm"
&& \  
rpm --rebuilddb && \  
yum -y install /tmp/java.rpm && \  
yum clean all && \  
rm -fr /tmp/*  
  
ENV JAVA_HOME=/usr/java/default  

