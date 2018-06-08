FROM mustardgrain/java8:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
ENV ZOOKEEPER_VERSION 3.4.8  
ENV ZOOKEEPER_URL
http://www.us.apache.org/dist/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz  
ENV ZOOKEEPER_HOME /opt/zookeeper-$ZOOKEEPER_VERSION  
  
RUN cd /opt && /usr/bin/curl -L -s $ZOOKEEPER_URL | tar xz  
  
COPY . /src  
  
RUN mkdir -p /etc/service/zookeeper && cp /src/run /etc/service/zookeeper  
  
WORKDIR $ZOOKEEPER_HOME  
  
EXPOSE 2181  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

