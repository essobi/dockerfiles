  
FROM centos:centos6  
  
MAINTAINER Hinling Yeung  
  
# Update the default application repository sources list  
RUN yum -y update  
  
# Install tar  
RUN yum -y install tar  
  
# Install java 1.6  
ENV JAVA_VERSION 1.6.0  
RUN yum -y install java-$JAVA_VERSION-openjdk  
RUN yum -y install java-$JAVA_VERSION-openjdk-devel.x86_64  
ENV JAVA_HOME /etc/alternatives/java_sdk_$JAVA_VERSION  
  
ENV AMQ_VERSION 5.6.0  
RUN curl -o /tmp/activemq.tar.gz
"http://archive.apache.org/dist/activemq/apache-activemq/$AMQ_VERSION/apache-
activemq-$AMQ_VERSION-bin.tar.gz"  
  
RUN gzip -d /tmp/activemq.tar.gz && cd /usr/local/ && tar xvf
/tmp/activemq.tar && ln -s /usr/local/apache-activemq-$AMQ_VERSION ./activemq  
  
# expose ports  
EXPOSE 8161  
EXPOSE 61613  
EXPOSE 61616  
ADD run.sh /run.sh  

