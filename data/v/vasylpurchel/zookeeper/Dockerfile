FROM ubuntu:trusty  
MAINTAINER Vasyl Purchel <vasyl.purchel@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y wget openjdk-7-jre-headless \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget http://www.eu.apache.org/dist/zookeeper/stable/zookeeper-3.4.7.tar.gz
\  
&& wget
http://www.eu.apache.org/dist/zookeeper/stable/zookeeper-3.4.7.tar.gz.md5 \  
&& md5sum zookeeper-3.4.7.tar.gz \  
&& tar xzf zookeeper-3.4.7.tar.gz -C /opt \  
&& mv /opt/zookeeper-3.4.7 /opt/zookeeper  
  
ADD zoo.cfg /opt/zookeeper/conf/  
  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/zookeeper/bin
\  
ZOOKEEPER_HOME=/opt/zookeeper \  
ZOOKEEPER_CONFIG_FILE=/opt/zookeeper/conf/zoo.cfg \  
ZK_DATA_DIR=/tmp/zookeeper  
  
ADD docker-entry-point.sh /opt/zookeeper/  
ENTRYPOINT ["/opt/zookeeper/docker-entry-point.sh"]  
CMD ["zkServer.sh", "start-foreground"]  

