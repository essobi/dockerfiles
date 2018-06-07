FROM java:8-jre  
  
MAINTAINER PalSzak  
  
RUN wget -q -O -
http://mirror.vorboss.net/apache/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
| tar -xzf - -C /opt  
RUN mv /opt/zookeeper-3.4.6/conf/zoo_sample.cfg
/opt/zookeeper-3.4.6/conf/zoo.cfg  
  
ENV ZK_HOME /opt/zookeeper-3.4.6  
ENV PATH /opt/zookeeper-3.4.6/bin:$PATH  
  
RUN sed -i "s|/tmp/zookeeper|$ZK_HOME/data|g" $ZK_HOME/conf/zoo.cfg; mkdir
$ZK_HOME/data  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
COPY ./image/conf /opt/zookeeper-3.4.6/conf  
VOLUME ["/opt/zookeeper-3.4.6/conf", "/opt/zookeeper-3.4.6/data"]  
  
EXPOSE 2181 2888 3888  
CMD ["zkServer.sh", "start-foreground"]  

