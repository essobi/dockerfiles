FROM openjdk:8-alpine  
  
LABEL maintainer="Arnaud Deprez <arnaudeprez@gmail.com>"  
  
ENV ACTIVEMQ_VERSION=5.15.0  
ENV ACTIVEMQ=apache-activemq-$ACTIVEMQ_VERSION  
ENV ACTIVEMQ_HOME=/opt/activemq  
  
RUN apk add --no-cache curl && \  
curl -sSL
https://archive.apache.org/dist/activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-
bin.tar.gz -o /tmp/$ACTIVEMQ-bin.tar.gz && \  
mkdir -p /opt && \  
tar -xzf /tmp/$ACTIVEMQ-bin.tar.gz -C /opt/ && \  
rm /tmp/$ACTIVEMQ-bin.tar.gz && \  
ln -s /opt/$ACTIVEMQ $ACTIVEMQ_HOME &&\  
rm -rf /opt/apache-activemq/examples && \  
rm -rf /opt/apache-activemq/docs && \  
rm -rf /opt/apache-activemq/webapps-demo  
  
#ADD ./activemq.xml $ACTIVEMQ_HOME/conf/activemq.xml  
# stomp, ws, nio, amqp, mqtt, http  
EXPOSE 61613 61614 61616 5672 1883 8161  
ENTRYPOINT ["/opt/activemq/bin/activemq"]  
CMD ["console"]  

