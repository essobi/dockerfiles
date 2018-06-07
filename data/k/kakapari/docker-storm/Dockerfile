# Docker File  
FROM centos:6  
ENV STORM_VERSION 1.0.2  
ENV ZK_VERSION 3.4.8  
ENV WK_COUNT 2  
ENV WK_PORT 6700  
# Install Java and python tools  
RUN yum -y install java-1.7.0-openjdk python-setuptools  
  
# Install Zookeeper  
ADD
http://mirror.fibergrid.in/apache/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz
/tmp  
RUN tar -zxf /tmp/zookeeper-${ZK_VERSION}.tar.gz -C /opt/ && mv
/opt/zookeeper-${ZK_VERSION} /opt/zookeeper && rm
/tmp/zookeeper-${ZK_VERSION}.tar.gz  
ADD conf/zoo.cfg /opt/zookeeper/conf/  
RUN mkdir -p /var/lib/zookeeper && echo 1 > /var/lib/zookeeper/myid  
  
# Install Storm  
ADD http://redrockdigimark.com/apachemirror/storm/apache-
storm-${STORM_VERSION}/apache-storm-${STORM_VERSION}.tar.gz /tmp  
RUN tar -zxf /tmp/apache-storm-${STORM_VERSION}.tar.gz -C /opt/ && mv
/opt/apache-storm-${STORM_VERSION} /opt/storm && rm /tmp/apache-
storm-${STORM_VERSION}.tar.gz  
ADD conf/storm.yaml /opt/storm/conf/  
  
# install supervisord  
RUN easy_install pip && pip install meld3==0.6.7 supervisor==3.0.0  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 8080 6627 8000  
CMD ["/usr/bin/supervisord"]  

