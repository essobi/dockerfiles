FROM debian:stable  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update; apt-get install -y openjdk-7-jre-headless wget  
  
ADD md5sums /opt/md5sums  
RUN cd /opt && \  
wget -q
http://mirror.softaculous.com/apache/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
&& \  
md5sum -c md5sums && \  
tar xzf zookeeper-3.4.6.tar.gz  
RUN mv /opt/zookeeper-3.4.6/conf/zoo_sample.cfg
/opt/zookeeper-3.4.6/conf/zoo.cfg  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
ENV ZK_HOME /opt/zookeeper-3.4.6  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper-3.4.6  
  
CMD ["bin/zkServer.sh", "start-foreground"]  

