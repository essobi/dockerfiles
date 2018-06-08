FROM misakai/java  
MAINTAINER Roman Atachiants "roman@misakai.com"  
ENV KAFKA_SCALA_VERSION 2.9.2  
ENV KAFKA_VERSION 0.8.1.1  
ENV KAFKA_RELEASE $KAFKA_SCALA_VERSION-$KAFKA_VERSION  
ENV KAFKA_HOME /opt/kafka_$KAFKA_RELEASE  
  
ADD
http://www.eu.apache.org/dist/kafka/$KAFKA_VERSION/kafka_$KAFKA_RELEASE.tgz
/opt/  
RUN tar zxvf /opt/kafka_$KAFKA_RELEASE.tgz -C /opt/  
  
ADD server.properties $KAFKA_HOME/config/server.properties  
ADD start.sh /start.sh  
  
CMD ["/start.sh"]  

