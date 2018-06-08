# DOCKER-VERSION 1.0.1  
# VERSION 0.1  
FROM centos:6.6  
MAINTAINER Pradeep Aradhya "pradeep4aradhya@gmail.com"  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum -y update && yum clean all  
  
RUN yum install -y java-1.7.0-openjdk.x86_64 java-1.7.0-openjdk-devel.x86_64
wget tar  
RUN wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-3.4.6 /opt/zookeeper \  
&& cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \  
&& mkdir -p /tmp/zookeeper  
  
ENV JAVA_HOME /usr/lib/jvm/jre-1.7.0-openjdk.x86_64  
  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper  
  
VOLUME ["/opt/zookeeper/conf", "/tmp/zookeeper"]  
  
ENTRYPOINT ["/opt/zookeeper/bin/zkServer.sh"]

