FROM mustardgrain/java8:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
ENV KAFKA_VERSION 0.10.2.0  
ENV KAFKA_LONG_VERSION kafka_2.12-$KAFKA_VERSION  
ENV KAFKA_URL
http://www.us.apache.org/dist/kafka/$KAFKA_VERSION/$KAFKA_LONG_VERSION.tgz  
ENV KAFKA_HOME /opt/$KAFKA_LONG_VERSION  
  
RUN cd /opt && /usr/bin/curl -L -s $KAFKA_URL | tar xz  
  
COPY . /src  
  
RUN mkdir -p /etc/service/kafka && cp /src/run /etc/service/kafka  
  
WORKDIR $KAFKA_HOME  
  
EXPOSE 9092  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

