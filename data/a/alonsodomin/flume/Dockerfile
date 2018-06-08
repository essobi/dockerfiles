FROM java:8-jre  
  
MAINTAINER Antonio Alonso Dominguez  
  
ENV FLUME_VERSION 1.6.0  
ENV FLUME_HOME /opt/lib/flume  
  
RUN mkdir -p /opt/lib && \  
wget -nv http://apache.websitebeheerjd.nl/flume/$FLUME_VERSION/apache-
flume-$FLUME_VERSION-bin.tar.gz -O /opt/lib/apache-flume-$FLUME_VERSION-
bin.tar.gz && \  
tar xzf /opt/lib/apache-flume-$FLUME_VERSION-bin.tar.gz -C /opt/lib && \  
mv /opt/lib/apache-flume-$FLUME_VERSION-bin /opt/lib/flume && \  
rm /opt/lib/apache-flume-$FLUME_VERSION-bin.tar.gz && \  
mv $FLUME_HOME/conf/flume-conf.properties.template $FLUME_HOME/conf/flume-
conf.properties  
  
VOLUME [ "/opt/lib/flume/conf" ]  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

