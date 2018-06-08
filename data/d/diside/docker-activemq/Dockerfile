FROM java:openjdk-8-jdk-alpine  
MAINTAINER diside <https://github.com/dilbertside/docker-activemq>  
ARG ACTIVEMQ_VERSION  
ENV ACTIVEMQ_VERSION ${ACTIVEMQ_VERSION:-5.14.0}  
LABEL Description="Light footprint ActiveMQ with openjdk-8-jdk-alpine"
Version="$ACTIVEMQ_VERSION"  
RUN echo "using activemq version $ACTIVEMQ_VERSION"  
ENV ACTIVEMQ apache-activemq-$ACTIVEMQ_VERSION  
ENV ACTIVEMQ_TCP=61616 ACTIVEMQ_AMQP=5672 ACTIVEMQ_STOMP=61613
ACTIVEMQ_MQTT=1883 ACTIVEMQ_WS=61614 ACTIVEMQ_UI=8161  
ENV ACTIVEMQ_HOME /var/lib/activemq  
  
#COPY "$ACTIVEMQ-bin.tar.gz" /tmp  
RUN \  
mkdir -p /var/lib && \  
wget -q -O /tmp/$ACTIVEMQ-bin.tar.gz -P /tmp
http://archive.apache.org/dist/activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-bin.tar.gz
&& \  
tar zxf /tmp/"$ACTIVEMQ-bin.tar.gz" -C /var/lib/ && \  
rm /tmp/"$ACTIVEMQ-bin.tar.gz" && \  
ln -s /var/lib/$ACTIVEMQ $ACTIVEMQ_HOME && \  
addgroup activemq && \  
adduser -S -H -h $ACTIVEMQ_HOME activemq activemq && \  
chown -R activemq:activemq /var/lib/$ACTIVEMQ  
  
USER activemq  
  
WORKDIR $ACTIVEMQ_HOME  
VOLUME ["/var/lib/$ACTIVEMQ/conf", "/var/lib/$ACTIVEMQ/data"]  
#RUN ls -lha /var/lib/  
#RUN ls -lha /var/lib/$ACTIVEMQ  
EXPOSE $ACTIVEMQ_TCP $ACTIVEMQ_AMQP $ACTIVEMQ_STOMP $ACTIVEMQ_MQTT
$ACTIVEMQ_WS $ACTIVEMQ_UI  
  
CMD ["/bin/sh", "-c", "bin/activemq console"]  

