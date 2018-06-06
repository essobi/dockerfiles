FROM ciscocloud/consul-template  
  
MAINTAINER Miguel Angel Guillen <miguitas@gmail.com>  
  
ENV ZOOKEEPER_VERSION 3.4.6  
ENV ZK_DATA_DIR /var/lib/zookeeper  
ENV ZK_LOG_DIR /var/log/zookeeper  
  
RUN apk-install bash openjdk7-jre  
  
ADD templates /consul-template/templates/  
  
RUN mkdir -p /opt  
  
RUN wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-$ZOOKEEPER_VERSION /opt/zookeeper \  
&& cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \  
&& mkdir -p /tmp/zookeeper  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
  
EXPOSE 2181 2888 3888  
COPY zk_config.sh /usr/local/bin/  
COPY zk_launch.sh /usr/local/bin/  
COPY setacl.sh /usr/local/bin/  
  
WORKDIR /opt/zookeeper  
  
VOLUME ["/var/lib/zookeeper", "/var/log/zookeeper"]  
  
ENTRYPOINT ["zk_config.sh"]  
  

