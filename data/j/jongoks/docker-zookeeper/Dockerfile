FROM jongoks/docker-jdk  
  
ENV ZOOKEEPER_VERSION 3.4.10  
#Download Zookeeper  
RUN wget -q
http://mirror.vorboss.net/apache/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz  
  
#Install  
RUN tar -xzf zookeeper-${ZOOKEEPER_VERSION}.tar.gz -C /opt  
  
#Configure  
RUN mv /opt/zookeeper-${ZOOKEEPER_VERSION}/conf/zoo_sample.cfg
/opt/zookeeper-${ZOOKEEPER_VERSION}/conf/zoo.cfg  
  
ENV ZK_HOME /opt/zookeeper-${ZOOKEEPER_VERSION}  
RUN sed -i "s|/tmp/zookeeper|$ZK_HOME/data|g" $ZK_HOME/conf/zoo.cfg; mkdir
$ZK_HOME/data  
RUN sed -i -r 's|#(log4j.appender.ROLLINGFILE.MaxBackupIndex.*)|\1|g'
$ZK_HOME/conf/log4j.properties  
RUN sed -i -r 's|#autopurge|autopurge|g' $ZK_HOME/conf/zoo.cfg  
  
EXPOSE 2181  
ENV PATH=$PATH:/opt/zookeeper-${ZOOKEEPER_VERSION}/bin  
  
WORKDIR /opt/zookeeper-${ZOOKEEPER_VERSION}  
  
CMD ["zkServer.sh", "start-foreground"]  

