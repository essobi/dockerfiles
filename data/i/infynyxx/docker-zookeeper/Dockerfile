FROM azul/zulu-openjdk:8  
RUN apt-get -y update && apt-get -y upgrade  
  
RUN apt-get -y install build-essential  
  
RUN apt-get -y install wget  
  
RUN wget -q -O -
http://mirror.vorboss.net/apache/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
| tar -xzf - -C /opt  
  
ENV ZK_HOME /opt/zookeeper-3.4.6  
RUN mkdir -p /data/zookeeper && mkdir -p /var/log/zookeeper  
  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper-3.4.6  
  
COPY *.cfg /opt/zookeeper-3.4.6/conf/  
  
COPY *.properties /opt/zookeeper-3.4.6/conf/  
  
CMD ["ZOO_LOG_DIR=/var/log/zookeeper", "ZOO_LOG4J_PROP=DEBUG,ROLLINGFILE",
"bash", "bin/zkServer.sh", "start"]  

