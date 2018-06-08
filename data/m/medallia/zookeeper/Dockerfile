FROM java:8  
MAINTAINER Cloud Fabric <cloud-fabric@medallia.com>  
  
RUN apt-get update && apt-get install -y openjdk-8-jdk wget \  
python2.7 libsvn-dev libapr1-dev # Aurora dependencies  
  
RUN wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.8/zookeeper-3.4.8.tar.gz
| tar -xzf - -C /usr/share \  
&& mv /usr/share/zookeeper-3.4.8 /usr/share/zookeeper  
  
ENV ZOO_LOG4J_PROP INFO,CONSOLE  
ENV DATADIR /opt/zookeeper/data  
ENV LOGDIR /opt/zookeeper/log  
ENV CONFDIR /opt/zookeeper/conf  
ENV CLIENTPORT 2181  
ENV INITLIMIT 5  
ENV SYNCLIMIT 2  
ENV CNXTIMEOUT 5000  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper  
  
VOLUME ["/opt/zookeeper"]  
  
ADD run.sh /  
  
ENTRYPOINT ["/run.sh"]  
CMD ["start-foreground", "/opt/zookeeper/conf/zoo.cfg"]  

