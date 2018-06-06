FROM ping2ravi/jdk:oracle_jdk8.92.14_ubuntu.15.10  
  
  
MAINTAINER Ravi Sharma  
# Ubuntu 15.10  
# Java Version oracle_jdk8 update 92  
# Zookeeper Version 3.4.8  
# http://zookeeper.apache.org/doc/r3.4.8/releasenotes.html  
ENV ZOOKEEPER_VERSION 3.4.8  
ENV ZOOKEEPER_HOME /opt/zookeeper/zookeeper-${ZOOKEEPER_VERSION}  
RUN sudo su; wget
http://mirrors.muzzy.org.uk/apache/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz
; gunzip zookeeper-${ZOOKEEPER_VERSION}.tar.gz ; tar -xvf
zookeeper-${ZOOKEEPER_VERSION}.tar; mkdir -p ${ZOOKEEPER_HOME}; mv
zookeeper-${ZOOKEEPER_VERSION}/* ${ZOOKEEPER_HOME} ; echo ${PATH}; echo
${ZOOKEEPER_HOME}/bin; rm zookeeper-${ZOOKEEPER_VERSION}.tar ; rm -fR
zookeeper-${ZOOKEEPER_VERSION}; cp ${ZOOKEEPER_HOME}/conf/zoo_sample.cfg
${ZOOKEEPER_HOME}/conf/zoo.cfg  
EXPOSE 2181  
ENV PATH ${PATH}:${JAVA_HOME}/bin:${ZOOKEEPER_HOME}/bin:${STORM_HOME}/bin  
CMD zkServer.sh start-foreground  

