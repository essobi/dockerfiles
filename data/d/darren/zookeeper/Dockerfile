FROM java:jre  
  
ENV ZK_VER 3.4.6  
RUN curl -L
"http://apache.mirrors.pair.com/zookeeper/zookeeper-$ZK_VER/zookeeper-$ZK_VER.tar.gz"
\  
| tar -xzf - -C /usr/local \  
&& cp /usr/local/zookeeper-$ZK_VER/conf/zoo_sample.cfg
/usr/local/zookeeper-$ZK_VER/conf/zoo.cfg \  
&& ln -s /usr/local/zookeeper-$ZK_VER /usr/local/zookeeper  
  
EXPOSE 2181  
CMD ["/usr/local/zookeeper/bin/zkServer.sh", "start-foreground"]  

