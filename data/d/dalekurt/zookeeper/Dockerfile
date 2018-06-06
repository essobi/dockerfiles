# ZooKeeper for Ubuntu 14.04  
#  
# GitHub - http://github.com/dalekurt/docker-zookeeper  
# Docker Hub - http://hub.docker.com/u/dalekurt/docker-zookeeper  
# Twitter - http://www.twitter.com/dalekurt  
FROM stackbrew/ubuntu  
  
MAINTAINER Dale-Kurt Murray "dalekurt.murray@gmail.com"  
# Basic environment setup  
RUN apt-get update && apt-get install -y wget openjdk-7-jre-headless  
  
# Downloading and install zookeeper  
RUN wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-3.4.6 /opt/zookeeper \  
&& cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \  
&& mkdir -p /tmp/zookeeper  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper  
  
VOLUME ["/opt/zookeeper/conf", "/tmp/zookeeper"]  
  
ENTRYPOINT ["/opt/zookeeper/bin/zkServer.sh"]  
CMD ["start-foreground"]  

