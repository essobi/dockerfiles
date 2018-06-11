FROM rboyer/base-java:centos6  
  
ENV ZOOKEEPER_VERSION 3.4.10  
RUN \  
wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz
| tar -xzf - -C /opt && \  
mv /opt/zookeeper-$ZOOKEEPER_VERSION /opt/zookeeper && \  
mkdir -p /zk/{config,data,logs}  
  
COPY log4j.properties /zk/config/log4j.properties  
COPY zoo.cfg /zk/config/zoo.cfg  
  
VOLUME ["/zk/config", "/zk/data", "/zk/logs"]  
EXPOSE 2181 2888 3888  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  

