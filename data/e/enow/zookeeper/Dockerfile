FROM enow/main  
  
MAINTAINER Writtic <writtic@gmail.com>  
  
# Latest version of Zookeeper  
ENV ZOOKEEPER_VERSION 3.4.8  
ENV ZK_HOME /usr/share/zookeeper  
# LABEL name="zookeeper" version=$ZOOKEEPER_VERSION  
# Download and Install Zookeeper  
RUN wget -q -N http://mirror.apache-
kr.org/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz
&& \  
tar -xzvf zookeeper-$ZOOKEEPER_VERSION.tar.gz -C /usr/share && mv
/usr/share/zookeeper-$ZOOKEEPER_VERSION $ZK_HOME && \  
rm -rf zookeeper-$ZOOKEEPER_VERSION.tar.gz && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Configure  
RUN mv $ZK_HOME/conf/zoo_sample.cfg $ZK_HOME/conf/zoo.cfg  
RUN sed -i "s|/tmp/zookeeper|$ZK_HOME/data|g" $ZK_HOME/conf/zoo.cfg; mkdir
$ZK_HOME/data  
  
ADD start-zk.sh $ZK_HOME/bin/start-zk.sh  
EXPOSE 2181 2888 3888  
WORKDIR /usr/share/zookeeper  
VOLUME ["/usr/share/zookeeper/conf", "/usr/share/zookeeper/data"]  
  
CMD /usr/sbin/sshd && bash $ZK_HOME/bin/start-zk.sh  

