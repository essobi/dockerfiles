FROM lhcpig/java:latest  
MAINTAINER lhcpig <lhcpig@qq.com>  
  
ENV ACTIVEMQ_VERSION 5.12.0  
ENV ACTIVEMQ apache-activemq-$ACTIVEMQ_VERSION  
  
# Expose all port  
EXPOSE 8161  
EXPOSE 61616  
EXPOSE 5672  
EXPOSE 61613  
EXPOSE 1883  
EXPOSE 61614  
# Expose some folders  
#VOLUME ["/data/activemq"]  
VOLUME ["/opt/activemq/data"]  
#VOLUME ["/opt/activemq/conf"]  
RUN mkdir -p /opt/activemq  
WORKDIR /opt/activemq  
RUN \  
curl http://supergsego.com/apache/activemq/$ACTIVEMQ_VERSION/apache-
activemq-$ACTIVEMQ_VERSION-bin.tar.gz | tar zx && \  
cp -rf $ACTIVEMQ/* /opt/activemq && \  
rm -rf $ACTIVEMQ  
  
CMD ["/bin/bash", "-c", "/opt/activemq/bin/activemq console"]

